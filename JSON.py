# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:32:44 2020

@author: jesus
"""
import json

data = '''{
            "name":"Chuck",
            "phone" : { "type" : "intl", "number":"+1 734 303 4456"},
            "email": {"hide":"yes"}
            }'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info['email']['hide'])