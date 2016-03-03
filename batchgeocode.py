#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
#import codecs
from pygeocoder import Geocoder, GeocoderResult

def geocode():
	
	src = open("src.csv","r")
	wfile = open("resultgeo.csv","w")
	writer = csv.writer(wfile)
	reader = csv.reader(src)
	header = next(reader)
	
	header.append("lat")	
	header.append("lng")

	writer.writerow(header)

	geocoder = Geocoder()

	rows = []
	for data in reader:
		print(data)
		print(data[1])
		result = geocoder.geocode(data[1], language="ja")
		row = [data[0],data[1],result.coordinates[0],result.coordinates[1]]
		rows.append(row)
		result = geocoder.reverse_geocode(*result.coordinates, language="ja")
		print(result)

	print(rows)
	writer.writerows(rows)
	wfile.close()
	src.close()

if __name__ == "__main__":
	geocode()


