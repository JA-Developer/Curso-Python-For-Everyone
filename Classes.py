# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 23:50:59 2020

@author: jesus
"""

class PartyAnimal:
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

print("Type", type(an))
print("Dir", dir(an))