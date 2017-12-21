package main

import (
	"encoding/xml"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"math"
	"math/rand"
	"os"
	"os/exec"
	"strconv"
	"sync"
	"time"
)

type JetAlgorithm func(j1, j2 Jet, deltaR float64) float64

func AntiKt(j1, j2 Jet, deltaR float64) float64 {
	if 1/j1.Sum.Pop > 1/j2.Sum.Pop {
		return deltaR / (j2.Sum.Pop*j2.Sum.Pop)
	}
	return deltaR / (j1.Sum.Pop*j1.Sum.Pop)
}

func Kt(j1, j2 Jet, deltaR float64) float64 {
	if j1.Sum.Pop > j2.Sum.Pop {
		return deltaR * j2.Sum.Pop*j2.Sum.Pop
	}
	return deltaR * j1.Sum.Pop*j1.Sum.Pop
}

type City struct {
	ID   int     `xml:"ville_id"`
	Name string  `xml:"ville_nom_simple"`
	Pop  float64 `xml:"ville_population_2012"`
	Lat  float64 `xml:"ville_latitude_deg"`
	Lon  float64 `xml:"ville_longitude_deg"`
	Dep  int     `xml:"ville_departement"`
}

type Jet struct {
	Sum          City
	Constituents []City
	Option       string
}

func main() {
	beg := time.Now()
	defer func() {
		delta := time.Since(beg)
		log.Printf("processing took: %v\n", delta)
	}()
	var wg sync.WaitGroup

	fname := "villes_france.xml"
	if len(os.Args) > 1 {
		fname = os.Args[1]
	}

	cities := loadCities(fname)
	log.Printf("cities: %8d\n", len(cities))
	//cities0 := selectCities(cities, 0, 1000)
	//cities1 := selectCities(cities, 1000, 10000)
	//cities2 := selectCities(cities, 10000, 100000)
	//cities3 := selectCities(cities, 100000, 1000000000)

	//log.Printf("cities-0: %8d\n", len(cities0))
	//log.Printf("cities-1: %8d\n", len(cities1))
	//log.Printf("cities-2: %8d\n", len(cities2))
	//log.Printf("cities-3: %8d\n", len(cities3))

	jets := make([]Jet, 0, len(cities))
	for _, city := range cities {
		jets = append(jets,
			Jet{
				Sum:          city,
				Constituents: []City{city},
				Option:       getColor(),
			},
		)
	}

	curSize := len(jets)
	oldSize := 0
	ifirst := 0
	var i1min_2ndBest =[]int{-1,-1}
	var i2min_2ndBest =[]int{-1,-1}
	var dRMin_2ndBest =[]float64{1e9,1e9}
	n_tentative :=1
	for curSize > 0 && (oldSize != curSize || n_tentative<2){
		if oldSize == curSize{
			n_tentative+=1
		}else{
			n_tentative=1
		}
		oldSize = curSize
		jets, ifirst, i1min_2ndBest, i2min_2ndBest, dRMin_2ndBest = findJet(jets, AntiKt, 100, ifirst, i1min_2ndBest, i2min_2ndBest, dRMin_2ndBest)
		curSize = len(jets)

		log.Printf("still %d cities to process (%d)...\n", len(jets), n_tentative)
		if curSize%100 == 0 {
			wg.Add(1)
			err := dumpBaseMap(jets, &wg)
			if err != nil {
				log.Fatalf("error dumping basemap: %v\n", err)
			}
			log.Printf("map done\n")
		}
	}

	wg.Wait()
}

func loadCities(fname string) []City {
	f, err := os.Open(fname)
	if err != nil {
		log.Fatalf("error opening file [%s]: %v\n", fname, err)
	}
	defer f.Close()

	var (
		cities []City
		latmax = 0.0
		latmin = 0.0
		lonmin = 0.0
		lonmax = 0.0
	)

	dec := xml.NewDecoder(f)
	for {
		// Read tokens from the XML document in a stream.
		t, err := dec.Token()
		if err != nil {
			if err != io.EOF {
				log.Fatalf("error decoding token: %v\n", err)
			}
			break
		}
		if t == nil {
			break
		}

		switch se := t.(type) {
		case xml.StartElement:
			if se.Name.Local == "table" {
				var table Table
				err = dec.DecodeElement(&table, &se)
				if err != nil {
					log.Fatalf("error decoding 'table' element: %v\n", err)
				}
				city := newCity(table)
				if !(city.Name != "" && city.Dep < 100 && city.Pop > 0) {
					continue
				}
				cities = append(cities, city)
				if city.Lon < lonmin {
					lonmin = city.Lon
				}
				if city.Lon > lonmax {
					lonmax = city.Lon
				}
				if city.Lat < latmin {
					latmin = city.Lat
				}
				if city.Lat > latmax {
					latmax = city.Lat
				}
			}
		}
	}

	log.Printf("cities: %d\n", len(cities))
	log.Printf("lon min=%8.3f max=%8.3f\n", lonmin, lonmax)
	log.Printf("lat min=%8.3f max=%8.3f\n", latmin, latmax)
	return cities
}

func selectCities(cities []City, min, max float64) []City {
	var sample []City
	for _, city := range cities {
		if min <= city.Pop && city.Pop < max {
			sample = append(sample, city)
		}
	}
	return sample
}

type Table struct {
	Name string   `xml:"name,attr"`
	Cols []Column `xml:"column"`
}

type Column struct {
	Name  string `xml:"name,attr"`
	Value string `xml:",chardata"`
}

func newCity(t Table) City {
	var err error
	var city City
	for _, col := range t.Cols {
		switch col.Name {
		case "ville_id":
			city.ID, err = strconv.Atoi(col.Value)
			if err != nil {
				log.Fatalf(
					"error decoding integer value (ID=%q): %v\n",
					col.Value,
					err,
				)
			}

		case "ville_departement":
			if col.Value == "2A" || col.Value == "2B" {
				col.Value = "2"
			}
			city.Dep, err = strconv.Atoi(col.Value)
			if err != nil {
				log.Fatalf(
					"error decoding integer value (dep=%q): %v\n",
					col.Value,
					err,
				)
			}

		case "ville_nom_simple":
			city.Name = col.Value
		case "ville_population_2012":
			city.Pop, err = strconv.ParseFloat(col.Value, 64)
			if err != nil {
				log.Fatalf(
					"error decoding float value (population=%q): %v\n",
					col.Value,
					err,
				)
			}

		case "ville_latitude_deg":
			city.Lat, err = strconv.ParseFloat(col.Value, 64)
			if err != nil {
				log.Fatalf(
					"error decoding float value (latitude=%q): %v\n",
					col.Value,
					err,
				)
			}

		case "ville_longitude_deg":
			city.Lon, err = strconv.ParseFloat(col.Value, 64)
			if err != nil {
				log.Fatalf(
					"error decoding float value (longitude=%q): %v\n",
					col.Value,
					err,
				)
			}
		}
	}
	return city
}

func findJet(jets []Jet, alg JetAlgorithm, dRMax float64, ifirst int, i1second, i2second []int, drsecond []float64) ([]Jet, int, []int, []int, []float64) {
	i1 := i1second[0]
	if i1<0{i1=0}
	i1min := -1
	i2min := -1
	dRMin := drsecond[0]
	i1min_prev := i1second[0]
	i2min_prev := i2second[0]
	dRMin_prev := drsecond[0]
	i1min_prev2 := i1second[1]
	i2min_prev2 := i2second[1]
	dRMin_prev2 := drsecond[1]
	dRMax2 := dRMax * dRMax

	tobreak := false
	log.Printf("findJet with i1=%d\n",i1,)

	for _, jet1 := range jets[i1:] {
		i2 := i1+1
		for _, jet2 := range jets[i1+1:] {
			if i2 <= i1 {
				i2++
				continue
			}
			if i2 != ifirst && i2 < i2second[0] {
				i2++
				continue
			}
			

			lat := jet1.Sum.Lat - jet2.Sum.Lat
			lon := (jet1.Sum.Lon - jet2.Sum.Lon) * math.Cos((jet1.Sum.Lat+jet2.Sum.Lat)*0.5 * math.Pi / 180.)
			dR := lat*lat + lon*lon
			dR *= 10000.0 / 90.0
			dR *= 10000.0 / 90.0 // in km

			if dR > dRMax2 {
				continue
			}

			dRCut := alg(jet1, jet2, dR)
			if dRCut <= dRMin {
				i1min_prev2 = i1min_prev
				i2min_prev2 = i2min_prev
				dRMin_prev2 = dRMin_prev
				i1min_prev = i1min
				i2min_prev = i2min
				dRMin_prev = dRMin
				
				i1min = i1
				i2min = i2
				dRMin = dRCut
				
				if dR == 0.0 {
					tobreak = true
					break
				}
			}
			i2++
		}
		if tobreak {
			tobreak = false
			break
		}
		i1++
	}

	iname := 0
	ikeep := -1
	iremove := 0
	
	if i1min == -1{
		i1min = i1min_prev
		i2min = i2min_prev
		dRMin = dRMin_prev
		i1min_prev = i1min_prev2
		i2min_prev = i2min_prev2
		dRMin_prev = dRMin_prev2
		i1min_prev2=-1
		i2min_prev2=-1
		dRMin_prev2=1e9
	}
	
	if i1min >= 0 && i2min >= 0 {
		j1 := jets[i1min]
		j2 := jets[i2min]
		log.Printf(
			"merging  (idx=%d) and (idx=%d) -- dR-min=%v ie %q and %q...\n",
			i1min, i2min,
			math.Sqrt(dRMin),
			j1.Sum.Name, j2.Sum.Name,
		)
		// take the name of the biggest city
		if j1.Sum.Pop > j2.Sum.Pop {
			iname = i1min
		} else {
			iname = i2min
		}

		// take the place of the first city
		if i2min > i1min {
			ikeep = i1min
			iremove = i2min
		} else {
			ikeep = i2min
			iremove = i1min
		}

		var (
			newElement Jet
			badElement Jet
		)

		switch iname {
		case i1min:
			newElement = jets[i1min]
			badElement = jets[i2min]
		case i2min:
			newElement = jets[i2min]
			badElement = jets[i1min]
		}

		newElement.Constituents = append(
			newElement.Constituents,
			badElement.Constituents...,
		)

		newElement.Sum.Lat = (newElement.Sum.Lat*(newElement.Sum.Pop) + badElement.Sum.Lat*badElement.Sum.Pop) / (newElement.Sum.Pop+badElement.Sum.Pop)
		newElement.Sum.Lon = (newElement.Sum.Lon*(newElement.Sum.Pop) + badElement.Sum.Lon*badElement.Sum.Pop) / (newElement.Sum.Pop+badElement.Sum.Pop)
		newElement.Sum.Pop += badElement.Sum.Pop

		jets[ikeep] = newElement
		jets = append(jets[:iremove], jets[iremove+1:]...)
	}

	if (dRMin ==0 && ikeep>=0) { // speed up the process at the begining
		var i1min_2ndBest =[]int{ikeep,-1}
		var i2min_2ndBest =[]int{-1,-1}
		var dRMin_2ndBest =[]float64{0.,1e9}
		return jets, ikeep,  i1min_2ndBest, i2min_2ndBest, dRMin_2ndBest
	}
	if (dRMin ==0 && ikeep==-1) { // speed up the process at the begining
		var i1min_2ndBest =[]int{-1,-1}
		var i2min_2ndBest =[]int{-1,-1}
		var dRMin_2ndBest =[]float64{1e9,1e9}
		return jets, ikeep,  i1min_2ndBest, i2min_2ndBest, dRMin_2ndBest
	}
	if i1min_prev == -1 {
		var i1min_2ndBest =[]int{-1,-1}
		var i2min_2ndBest =[]int{-1,-1}
		var dRMin_2ndBest =[]float64{1e9,1e9}
		return jets, ikeep, i1min_2ndBest, i2min_2ndBest, dRMin_2ndBest
	}
	log.Printf(
			"Second best choice  (idx=%d , %d) -- dR-min=%v ...\n",
			i1min_prev,i2min_prev, math.Sqrt(dRMin_prev),
	)
	log.Printf(
			"Third best choice  (idx=%d , %d) -- dR-min=%v ...\n",
			i1min_prev2,i2min_prev2, math.Sqrt(dRMin_prev2),
	)
	
	var i1min_2ndBest =[]int{i1min_prev,i1min_prev2}
	var i2min_2ndBest =[]int{i2min_prev,i2min_prev2}
	var dRMin_2ndBest =[]float64{dRMin_prev,dRMin_prev2}
	
	return jets, ikeep, i1min_2ndBest, i2min_2ndBest,dRMin_2ndBest
}

func dumpBaseMap(jets []Jet, wg *sync.WaitGroup) error {
	var err error
	fname := fmt.Sprintf("data_fig_%06d_cities.txt", len(jets))
	out, err := os.Create(fname)
	if err != nil {
		return err
	}
	defer out.Close()

	for _, jet := range jets {
		//if jet.Sum.Pop < 5000 {
		//	continue
		//}
		if len(jet.Constituents) < 2 {
			continue
		}
		for _, city := range jet.Constituents {
			fmt.Fprintf(out, "%f;%f;%s\n", city.Lon, city.Lat, jet.Option)
		}
	}

	err = out.Close()
	if err != nil {
		return err
	}

	py := fmt.Sprintf(`#!/usr/bin/env python2
import sys
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
def main(fname):
	m = Basemap(projection='merc',llcrnrlat=41,urcrnrlat=52,
            llcrnrlon=-6,urcrnrlon=10,lat_ts=15,resolution='c')
	#m.drawmapboundary(fill_color='aqua')
	m.bluemarble()
	#m.drawcoastlines()
	#m.fillcontinents(color='coral',lake_color='aqua')
	m.drawparallels(np.arange(10,90,20))
	m.drawmeridians(np.arange(-180,180,30))
	m.drawcountries()
	for line in open(fname).readlines():
		values = line.strip().split(";")
		lon = float(values[0])
		lat = float(values[1])
		drawOpt = values[2]
		m.plot(lon, lat, drawOpt, latlon=True)
		pass
	
	plt.title("%[1]d cities")
	plt.savefig("fig_go_%[1]d.png")
	return
if __name__ == "__main__":
	main(%[2]q)
`,
		len(jets),
		fname,
	)
	go func(py, fname string, wg *sync.WaitGroup) {
		err := ioutil.WriteFile(fname+".py", []byte(py), 0644)
		if err != nil {
			log.Fatalf("error creating python script for [%s]: %v\n",
				fname,
				err,
			)
		}
		defer os.Remove(fname + ".py")

		cmd := exec.Command(
			"python2",
			fname+".py",
		)
		cmd.Stdin = os.Stdin
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		log.Printf(":: processing [%s]...\n", fname)
		err = cmd.Run()
		wg.Done()
		log.Printf(":: removing [%s]...\n", fname)
		if err != nil {
			errRm := os.Remove(fname)
			if errRm != nil {
				log.Printf("error removing data file [%s]: %v\n", fname, errRm)
			}
			log.Fatalf("error processing [%s]: %v\n", fname, err)
		}
		errRm := os.Remove(fname)
		if errRm != nil {
			log.Printf("error removing data file [%s]: %v\n", fname, errRm)
		}
	}(py, fname, wg)

	return err
}

var colors = []string{
	"og", "or", "ob", "oy",
	"+g", "+r", "+b", "+y",
	"*g", "*r", "*b", "*y",
	"xg", "xr", "xb", "xy",
}

func getColor() string {
	idx := rand.Intn(len(colors))
	return colors[idx]
}
