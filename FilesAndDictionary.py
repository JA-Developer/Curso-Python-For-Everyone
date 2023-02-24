# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 23:51:54 2020

@author: jesus
"""

counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Countings...')
for word in words:
    counts[word] = counts.get(word,0)+1
print('Counts', counts)