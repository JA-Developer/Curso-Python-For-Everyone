# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 00:43:27 2020

@author: jesus
"""

while True:
    cmd = input("Enter a command:").strip()
    EndOfWord = cmd.find(' ')
    if(EndOfWord == -1):
        if cmd.lower()=='exit':
            break
        else:
            print("Command unrecognized.")
    else:
        if cmd[:EndOfWord].lower()=='select':
            pass
        elif cmd[:EndOfWord].lower()=='update':
            pass
        elif cmd[:EndOfWord].lower()=='delete':
            pass
        else:
            print("Command unrecognized.")
            