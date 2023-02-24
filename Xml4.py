# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 18:02:08 2020

@author: jesus
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = input('Enter location: ')
print('Retrieving',url)
fhand = urllib.request.urlopen(url)

Text = fhand.read()

print('Retrieved', len(Text) ,'characters')

Tree = ET.fromstring(Text)

counts = Tree.findall('.//count')

number = 0
total = 0
for count in counts:
    number=number+1
    total = total + int(count.text)

print('Count:', number)
print('Sum:', total)