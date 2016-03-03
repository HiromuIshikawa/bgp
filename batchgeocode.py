#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import csv
#import codecs
from pygeocoder import Geocoder, GeocoderResult

def geocode(src,result):
	
	rfile = open(src,"r")
	wfile = open(result,"w")
	writer = csv.writer(wfile)
	reader = csv.reader(rfile)
	header = next(reader)
	
	header.append("lat")	
	header.append("lng")

	writer.writerow(header)

	geocoder = Geocoder()

	rows = []
	for data in reader:
		print("address:" + data[1] + " ...geocoding now")
		geo = geocoder.geocode(data[1], language="ja")
		if geo is not None :
			print("success... (lat,lng)=",end="")	
			row = [data[0],data[1],geo.coordinates[0],geo.coordinates[1]]
			rows.append(row)
			print(geo.coordinates)
		else:
			print("error...")

	writer.writerows(rows)
	wfile.close()
	rfile.close()

if __name__ == "__main__":
	param = sys.argv
	geocode(param[1],param[2])


