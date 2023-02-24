# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:15:02 2020

@author: jesus
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
Count = 0
Result = 0
for tag in tags:
    Result= Result + int(tag.contents[0])
    Count=Count+1
print('Count', Count)
print('Sum', Result)
    

