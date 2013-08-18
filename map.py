#!/usr/bin/python

import cgi

import cgitb
cgitb.enable()

LOCATION_FILENAME="chaz_location.txt"
    
#Read the location
try:
    (lat, long, alt) = open(LOCATION_FILENAME).readlines()
except ValueError as e:
    (lat, long, alt) = (0.0, 0.0, 0.0)
print(lat, long, alt)
