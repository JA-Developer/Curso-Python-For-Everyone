# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 01:24:59 2020

@author: jesus
"""

import json
import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;
                  
CREATE TABLE User(
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	Name TEXT UNIQUE
);

CREATE TABLE Course(
	Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	Title TEXT UNIQUE
);

CREATE TABLE Member(
	User_Id INTEGER,
	Course_Id INTEGER,
	Role INTEGER,
	PRIMARY KEY (User_Id, Course_Id)
);''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data_sample.json'

str_data = open(fname).read()
json_data = json.loads(str_data)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    
    print((name, title))
    
    cur.execute('''INSERT OR IGNORE INTO User(Name) VALUES (?)''', (name,))
    cur.execute('SELECT Id FROM User WHERE Name = ?', (name,))
    user_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR IGNORE INTO Course(Title) VALUES (?)''', (title,))
    cur.execute('SELECT Id FROM Course WHERE Title = ?', (title,))
    course_id = cur.fetchone()[0]
    
    cur.execute('''INSERT OR REPLACE INTO Member(User_Id, Course_Id) VALUES (?,?)''', (user_id, course_id,))
    
    conn.commit()