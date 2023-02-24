# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 00:37:02 2020

@author: jesus
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()

for line in handle:
    if line.startswith('From '):
        words = line.split()
        emails[words[1]] = emails.get(words[1],0)+1

MaxKey = None
MaxValue = None

for key, value in emails.items():
    if MaxValue is None or value > MaxValue:
        MaxValue = value
        MaxKey = key

print(MaxKey,MaxValue)