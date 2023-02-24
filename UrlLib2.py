# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:15:02 2020

@author: jesus
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Type your link: ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

