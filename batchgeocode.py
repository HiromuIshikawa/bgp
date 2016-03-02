#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import codecs
from pygeocoder import Geocoder, GeocoderResult

def geocode():
	
	src = open("src.txt","r")
	rfile = codecs.open("resultgeo.csv","w","utf-8")
	writer = csv.writer(rfile)

	rows = []
	row = ["lat","lng"]
	writer.writerow(row)
	geocoder = Geocoder()

	for address in src:
		print address
		result = geocoder.geocode(address, language="ja")
		rows.append([result.coordinates[0],result.coordinates[1]])
		print result
		result = geocoder.reverse_geocode(*result.coordinates, language="ja")
		print result

	writer.writerows(rows)
	rfile.close()
	src.close()
if __name__ == "__main__":
	geocode()


