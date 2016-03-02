#!/usr/bin/python
# -*- coding: utf-8 -*-

from pygeocoder import Geocoder, GeocoderResult


address = u'Japan, Okayama'
geocoder = Geocoder()

result = geocoder.geocode(address, language="ja")

print result.coordinates

result = geocoder.reverse_geocode(*result.coordinates, language="ja")

print result
