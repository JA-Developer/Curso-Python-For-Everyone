# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:46:26 2020

@author: jesus
"""

d={'a':10, 'b':1, 'c':22}

t = sorted(d.items())
print(t)
for k,v in sorted(d.items()):
    print(k,v)