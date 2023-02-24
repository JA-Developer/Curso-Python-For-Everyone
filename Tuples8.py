# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:46:26 2020

@author: jesus
"""

c = {'a':10, 'b':1, 'c':22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse = True)
print(tmp)