# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:02:28 2020

@author: jesus
"""

class PartyAnimal:
    x=0
    
    def __init__(self):
        print('I am constructed')
    
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
    
    def __del__(self):
        print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains', an)