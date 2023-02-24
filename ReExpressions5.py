# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:00:51 2020

@author: jesus
"""

import re

x='My 2 favorite numbers are 19 and 42'
y=re.findall('[0-9]+',x)
print(y)
y=re.findall('[AEIOU]+',x)
print(y)