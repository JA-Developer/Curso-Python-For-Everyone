# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:00:51 2020

@author: jesus
"""

import re

x='From: Using the : character'
y = re.findall('^F.+:', x)
print(y)