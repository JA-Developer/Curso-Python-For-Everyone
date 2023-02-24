# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 00:19:36 2020

@author: jesus
"""

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

address = input('Enter location: ')

url = serviceurl + urllib.parse.urlencode({'address': address, 'key': 42})
print('Retrieving',url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] !='OK':
    print('==== Failure To Retrieve ====')
    print(data)
else:
    PlaceId = js['results'][0]['place_id']
    print('Place id', PlaceId)