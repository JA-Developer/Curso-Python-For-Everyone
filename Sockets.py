# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:00:51 2020

@author: jesus
"""

import socket

sct = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sct.connect(('data.pr4e.org',80))
sct.send('GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode())

while True:
    data = sct.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
sct.close()
