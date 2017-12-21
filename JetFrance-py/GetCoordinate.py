#!/usr/bin/env python



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
			
			if float(ville[2])>latmax: latmax = float(ville[2])
			if float(ville[2])<latmin: latmin = float(ville[2])
			if float(ville[3])>lonmax: lonmax = float(ville[3])
			if float(ville[3])<lonmin: lonmin = float(ville[3])
	
		ville = ["",  0, 0, 0, 0]
			
	elif line.find("ville_nom_simple")!=-1:
		ville[0] = line[line.find('">')+2:line.find('</')]
		#print ville[0]
	elif line.find("ville_population_2012")!=-1:
		ville[1] = line[line.find('">')+2:line.find('</')]
		#print ville[1]
	elif line.find("ville_latitude_deg")!=-1:
		ville[2] = line[line.find('">')+2:line.find('</')]
		#print ville[2]
	elif line.find("ville_longitude_deg")!=-1:
		ville[3] = line[line.find('">')+2:line.find('</')]
		#print ville[3]
	elif line.find("ville_departement")!=-1:
		ville[4] = line[line.find('">')+2:line.find('</')]
		if ville[4]=="2A" or ville[4] =="2B":
			ville[4]="2"
		
		#print ville[4]
	
		
	i+=1
	#if i>firstline+150: break

for i in dico:
	print i

print len(dico),"villes"
print "longitudes:",lonmin,lonmax
print "latitudes:",latmin,latmax

