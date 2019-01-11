# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 00:21:46 2018

@author: TZLMYQ
"""


print "Practice makes Perfect!"   


given a location and area , return list of locations close to the location given.
Mark searched house yellow

API

S:  location -- coordinates. (long lat, zip, street/ city name/ state/ price / )
N: need 
  
A: api        long lat, zip, street/ city name/ state/ price /  property type / price/ area/ school di
  
      1) api(long, lat, search_range):
      48, 48
      48.123456,48.123456
      O(nlgn)
        return list of locations
      
      NoSQL
      MongoDB
      
      location -> document --> JSON
      document -> index
      geo index -> long/lat
      l1 - R, l2 - R, l1+R, l2 + R 
      
      index structure hashtable
      "48.123456,48.123456" -> document
      
      user db 10X    20 kb
      location db 2X   100k,  1mb 100 GB.
      20kb, 1 million, 20GB
      10X 
      200GB, 
      
      1 million, 0.1 million
      DAU -- peak QPS  1m / 24 / 3600 * 
      
      https://docs.mongodb.com/manual/tutorial/geospatial-tutorial/
K: data
E: evole
  
  
  lb -> servers