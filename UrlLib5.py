# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:15:02 2020

@author: jesus
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter URL: ')

count = int(input('Enter count: '))

position = int(input('Enter position: '))

name = ''
for iteration in range(count+1):
    print('Retrieving:',url)
    html = urllib.request.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[position-1].get('href', None)
    

