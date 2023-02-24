# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:00:51 2020

@author: jesus
"""

import re

x=open('regex_sum_812629.txt')
Suma = 0
for line in x:
    y = re.findall('[0-9]+', line)
    for number in y:
        Suma =Suma + int(number.strip())
print(Suma)