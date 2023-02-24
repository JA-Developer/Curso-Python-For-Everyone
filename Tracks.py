# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 03:09:55 2020

@author: jesus
"""

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('trackdb.sqlite')
cur = conn.cursor()

cur.executescript('''
                  DROP TABLE IF EXISTS Artist;
                  DROP TABLE IF EXISTS Album;
                  DROP TABLE IF EXISTS Track;
                  
                  CREATE TABLE Artist (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                       Name TEXT UNIQUE
                                       );
                  CREATE TABLE Album (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                      Artist_Id INTEGER,
                                      Title TEXT UNIQUE
                                      );
                  CREATE TABLE Track (Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                      Title TEXT UNIQUE,
                                      Album_Id INTEGER,
                                      Len INTEGER,
                                      Rating INTEGER,
                                      Count INTEGER
                                      );
                  ''')

fname = input('Enter file name: ')
if(len (fname)<1): fname ='Library.xml'

#<key>Track ID</key><integer>369</integer>
#<key>Name</key><string>Another One Bits The Dust</string>
#<key>Artist</key><string>Queen</string>

def  lookup(d,key):
    found = False
    for child in d:
        if found: return child.text
        if child.tag == 'key' and child.text==key:
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))
for entry in all:
    if(lookup(entry, 'Track ID') is None) : continue

    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    
    if name is None or artist is None or album is None:
        continue
    
    print(name, artist, album, count, rating, length)
    
    cur.execute ('''INSERT OR IGNORE INTO Artist (name)
                 VALUES (?)''', (artist,))
    cur.execute('SELECT Id FROM Artist WHERE Name = ?', (artist,))
    artist_id = cur.fetchone()[0]
    
    cur.execute ('''INSERT OR IGNORE INTO Album (title, Artist_Id)
                 VALUES (?, ?)''', (album, artist_id,))
    cur.execute('SELECT Id FROM Artist WHERE Name = ?', (artist,))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Track
                (Title, Album_Id,Len,Rating, Count)
                VALUES (?, ?, ?, ?, ?)''', (name, album_id, length, rating, count))
    
    conn.commit()