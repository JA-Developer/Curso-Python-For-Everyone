# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:15:02 2020

@author: jesus
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen('https://www.google.com')

counts = dict()

for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word,0)+1
print(counts)