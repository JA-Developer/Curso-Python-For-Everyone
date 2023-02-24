# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:00:51 2020

@author: jesus
"""

import re

x=open('regex_sum_812629.txt')
Suma = 0

print(sum([int(value) for value in re.findall('[0-9]+', x.read())]))
