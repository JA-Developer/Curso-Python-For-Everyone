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
                  DROP TABLE IF EXISTS Genre;
                  DROP TABLE IF EXISTS Album;
                  DROP TABLE IF EXISTS Track;
                  
                  CREATE TABLE Artist (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name    TEXT UNIQUE
                );
                
                CREATE TABLE Genre (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name    TEXT UNIQUE
                );
                
                CREATE TABLE Album (
                    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    artist_id  INTEGER,
                    title   TEXT UNIQUE
                );
                
                CREATE TABLE Track (
                    id  INTEGER NOT NULL PRIMARY KEY 
                        AUTOINCREMENT UNIQUE,
                    title TEXT  UNIQUE,
                    album_id  INTEGER,
                    genre_id  INTEGER,
                    len INTEGER, rating INTEGER, count INTEGER
                );
                  ''')

fname = input('Enter file name: ')
if(len (fname)<1): fname ='Library.xml'

#<key>Track ID</key><integer>369</integer>
#<key>Name</key><string>Another One Bits The Dust</string>
#<key>Artist</key><string>Queen</string>

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

for entry in all:
    if(lookup(entry, 'Track ID') is None) : continue

    name = lookup(entry, 'Name')
    genre = lookup(entry, 'Genre')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
    
    if name is None or artist is None or album is None or genre is None:
        continue
    
    print(name, genre, artist, album, count, rating, length)
    
    cur.execute ('''INSERT OR IGNORE INTO Artist (name)
                 VALUES (?)''', (artist,))
    cur.execute('SELECT Id FROM Artist WHERE Name = ?', (artist,))
    artist_id = cur.fetchone()[0]
    
    cur.execute ('''INSERT OR IGNORE INTO Genre (name)
                 VALUES (?)''', (genre,))
    cur.execute('SELECT Id FROM Genre WHERE Name = ?', (genre,))
    genre_id = cur.fetchone()[0]
    
    cur.execute ('''INSERT OR IGNORE INTO Album (title, Artist_Id)
                 VALUES (?, ?)''', (album, artist_id,))
    cur.execute('SELECT Id FROM Artist WHERE Name = ?', (artist,))
    album_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Track
                (Title, Album_Id,genre_id, Len,Rating, Count)
                VALUES (?, ?, ?, ?, ?, ?)''', (name, album_id, genre_id, length, rating, count))
    
    conn.commit()