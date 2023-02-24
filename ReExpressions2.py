# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:00:51 2020

@author: jesus
"""

import re

hand = open('mbox-short.txt')
for line in hand:
        line=line.rstrip()
        if re.search('^From:', line):
            print(line)