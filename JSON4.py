# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 00:19:36 2020

@author: jesus
"""

import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')

print('Retrieving',url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)

count = 0
total = 0

for element in js['comments']:
    count=count+1
    total = total + int(element["count"])

print('Count:',count)
print('Sum:',total)