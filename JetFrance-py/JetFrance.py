#!/usr/bin/env python

from math import *
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from random import randint


colors=['og', 'or', 'ob', 'oy',\
        '+g', '+r', '+b', '+y',\
        '*g', '*r', '*b', '*y',\
        'xg', 'xr', 'xb', 'xy' ]

def printFrance(List, drawOpt):
	m = Basemap(projection='merc',llcrnrlat=41,urcrnrlat=52,\
            llcrnrlon=-6,urcrnrlon=10,lat_ts=15,resolution='c')
	m.drawmapboundary(fill_color='aqua')
	m.drawcoastlines()
	m.fillcontinents(color='coral',lake_color='aqua')
	m.drawparallels(np.arange(10,90,20))
	m.drawmeridians(np.arange(-180,180,30))
	m.drawcountries()
	
	for [nom, popu, lat, lon, dept]	in List:
		if drawOpt=="random":
			m.plot(lon, lat, colors[randint(0,15)], latlon=True)
		else:
			m.plot(lon, lat, drawOpt, latlon=True)
	plt.title("title")
	plt.show()
	
	
def printFrances(Lists):
	m = Basemap(width=12000000,height=9000000, projection='merc',llcrnrlat=41,urcrnrlat=52,\
            llcrnrlon=-6,urcrnrlon=10,lat_ts=15,resolution='c')
	#m.drawmapboundary(fill_color='aqua')
	m.bluemarble()
	#m.drawcoastlines()
	#m.fillcontinents(color='coral',lake_color='aqua')
	m.drawparallels(np.arange(10,90,20))
	m.drawmeridians(np.arange(-180,180,30))
	m.drawcountries()
	i=0
	for [total, List, drawValue] in Lists:
		drawOpt=drawValue
		if drawOpt=="random":
			drawOpt=colors[randint(0,15)]
			Lists[i][2]=drawOpt	
		for [nom, popu, lat, lon, dept]	in List:
			m.plot(lon, lat, drawOpt, latlon=True)
		
		i+=1
		
	plt.title("title")
	#plt.show()
	plt.savefig("fig_"+`len(Lists)`+".png")
	return Lists
	
def getList(nMax=0):

	f = open("villes_france.xml", "r")

	i=0
	
	firstline=71
	
	dico = []
	ville = ["",  0, 0, 0, 0] # nom, popu, lat, longi, dept
	
	latmax=45
	latmin=45
	lonmin=10
	lonmax=0
	
	for l in f.readlines():
		line=l[:-1]
		i+=1
		if i<firstline: continue
		#print line
		
		if line.find("villes_france_free")!=-1 or line.find("database")!=-1:
			if ville[0]!="" and int(ville[4])<100:
				dico += [ville]
				
				if ville[2]>latmax: latmax = ville[2]
				if ville[2]<latmin: latmin = ville[2]
				if ville[3]>lonmax: lonmax = ville[3]
				if ville[3]<lonmin: lonmin = ville[3]
		
			ville = ["",  0, 0, 0, 0]
					
		elif line.find("ville_nom_simple")!=-1:
			ville[0] = line[line.find('">')+2:line.find('</')]
			#print ville[0]
		elif line.find("ville_population_2012")!=-1:
			ville[1] = float(line[line.find('">')+2:line.find('</')])
			#print ville[1]
		elif line.find("ville_latitude_deg")!=-1:
			ville[2] = float(line[line.find('">')+2:line.find('</')])
			#print ville[2]
		elif line.find("ville_longitude_deg")!=-1:
			ville[3] = float(line[line.find('">')+2:line.find('</')])
			#print ville[3]
		elif line.find("ville_departement")!=-1:
			ville[4] = line[line.find('">')+2:line.find('</')]
			if ville[4]=="2A" or ville[4] =="2B":
				ville[4]="2"
			
			#print ville[4]
			
		i+=1
		#if i>firstline+150: break
		if nMax and len(dico)>nMax:
			break
		
	#for i in dico:
	#	print i
	
	print len(dico),"villes"
	print "longitudes min/max:",lonmin,lonmax
	print "latitudes min/max:",latmin,latmax
	
	return dico
	
def findJet(Lists, algo, drmax):
	#print Lists[0]
	i1=0
	
	i1min=-1
	i2min=-1
	DRmin = 1e9
	tobreak = 0
	for [ville1, listOfVille1, drawOpt1] in Lists:
		N1   = ville1[1]
		if N1==0: continue
		lat1 = ville1[2]
		lon1 = ville1[3]
		i2=0
		for [ville2, listOfVille2, drawOpt2] in Lists:
			if ville1[0]==ville2[0]:
				continue
			N2   = ville2[1]
			if N2==0:continue
			lat2 = ville2[2]
			lon2 = ville2[3]
			dr = sqrt ( (lat1 - lat2)**2 + ((lon1 - lon2)*cos((lat1+lat2)/2))**2 ) # en mille nautique
			dr *= 10000/ 90
			
			if dr>drmax: continue
			
			#print lat1,lat2,dr
			DR = dr**2 * 1e6
			if algo=="antikt":
				if 1/N1>1/N2:
					DR *= 1/ (N2**2)
				else :
					DR *= 1/ (N1**2)
			if algo=="kt":
				if N1>N2:
					DR *= (N2**2)
				else :
					DR *= (N1**2)
			if DR<DRmin:
				print N1,N2,dr,DR
				i1min=i1
				i2min=i2
				DRmin=DR
				
				if dr==0.:
					print ville1
					print ville2
					tobreak = 1
					break
			i2+=1
		if tobreak: 
			tobreak=0
			break
		i1+=1
	
	if i1min>=0:
		element1 = Lists[i1min]
		element2 = Lists[i2min]
		print "Merging",element1
		print "  and  ",element2
		newElement = []
		i_keep=-1
		i_remove=-1
		if element1[0][1]>element2[0][1]: # take the name of the biggest city
			i_keep   = i1min
			i_remove = i2min
		else:
			i_keep   = i2min
			i_remove = i1min
		
		newElement = Lists[i_keep]
		badElement = Lists[i_remove]
		
		newElement[1]+=badElement[1]
		newElement[0][1]+=badElement[0][1] # add the number of inhabitants
		# new latitude
		newElement[0][2] = (newElement[0][2]*newElement[0][1]+badElement[0][2]*badElement[0][1])/(newElement[0][1]+badElement[0][1])
		newElement[0][3] = (newElement[0][3]*newElement[0][1]+badElement[0][3]*badElement[0][1])/(newElement[0][1]+badElement[0][1])
		
		print newElement
		
		Lists[i_keep] = newElement
		del Lists[i_remove]
	
	return Lists
	
def selectVilles(List, Min, Max):
	subList = []

	for [nom, popu, lat, lon, dept]	in List:
		if popu>=Min and popu <Max:
			subList += [[nom, popu, lat, lon, dept]]
	
	return subList
	
def main():
	List = getList(5000)
	
	list_0_1000 = selectVilles(List, 0, 1000)
	list_1000_10000 = selectVilles(List, 1000, 10000)
	list_10000_100000 = selectVilles(List, 10000, 100000)
	list_100000_inf = selectVilles(List, 100000, 1000000000)
	'''
	printFrance(list_0_1000, 'go')
	printFrance(list_1000_10000, 'bo')
	printFrance(list_10000_100000, 'yo')
	printFrance(list_100000_inf, 'ro')
	'''
	#printFrance(List, "random")
	
	if 0:
		Lists = []
		Lists +=[[list_0_1000, 'go']]
		Lists +=[[list_1000_10000, 'bo']]
		Lists +=[[list_10000_100000, 'yo']]
		Lists +=[[list_100000_inf, 'ro']]
	
		printFrances(Lists)
	
	if 0:
		Lists = []
		Lists +=[[list_0_1000, 'random']]
		Lists +=[[list_1000_10000, 'random']]
		Lists +=[[list_10000_100000, 'random']]
		Lists +=[[list_100000_inf, 'random']]
	
		printFrances(Lists)
	
	Lists = []
	for i in List:
		element = [i,[i,], "random"] #[sum of cities, list of cities, draw option]
		Lists += [element]
	
	tailleListe = len(Lists)
	oldtaille=0
	while tailleListe>4990 and oldtaille!=tailleListe:
		oldtaille = tailleListe
		Lists = findJet(Lists, "antikt", 100)
		tailleListe = len(Lists)
		print "Encore ",tailleListe,"villes!"
		if tailleListe%1==0:
			Lists = printFrances(Lists)

main()
