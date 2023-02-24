# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:00:51 2020

@author: jesus
"""

import re

x=open('mbox-short.txt')
for line in x:
    y = re.findall('@([^ ]*)', line)
    print(y)