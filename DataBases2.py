# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 22:51:32 2020

@author: jesus
"""

import sqlite3

conn = sqlite3.connect('organizations.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute ('CREATE TABLE Counts (org TEXT, count INTEGER)')
handle = open('mbox.txt')

Orgs = dict()

for line in handle:
    if line.startswith('From: '):
        pieces = line.split()
        organization = pieces[1][pieces[1].find('@')+1:].strip()
        Orgs[organization] = Orgs.get(organization,0)+1

for (k, v) in Orgs.items():
    cur.execute('INSERT INTO Counts VALUES(\'' + k + '\','+str(v)+')')
conn.commit()