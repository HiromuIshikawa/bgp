#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import csv
import pandas as pd
#import codecs
from pygeocoder import Geocoder, GeocoderResult

def geocode(src,result):
	
	rfile = pd.read_csv(src, skiprows=1, names=("name", "address", "lat", "lng"))
	print(rfile)

	geocoder = Geocoder()

#	rows = []
	for i in range(len(rfile)):
		print("address:" + rfile.ix[i,"address"] + " ...geocoding now")
		geo = geocoder.geocode(rfile.ix[i,"address"], language="ja")
		if geo is not None :
			print("success... (lat,lng)=",end="")	
			rfile.ix[i,["lat","lng"]] = geo.coordinates
			print(geo.coordinates)
			print(geocoder.reverse_geocode(geo.coordinates[0],geo.coordinates[1],language="ja"))
		else:
			print("error...")

	rfile.to_csv("test2.csv", index=False)
if __name__ == "__main__":
	param = sys.argv
	geocode(param[1],param[2])


