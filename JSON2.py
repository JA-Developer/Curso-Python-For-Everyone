# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:53:22 2020

@author: jesus
"""

import json
input = '''[
                {
                    "id":"001",
                    "x":"2",
                    "name":"Chuck"
                },
                {
                    "id":"009",
                    "x":"7",
                    "name":"Chuck"
                }
            ]
'''

info = json.loads(input)
print('User count:', len(info))
for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])