# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 20:20:33 2018

@author: niketanrane
Language Used : Python 3.6.5

"""

#ex14
from sys import argv
script = argv
prompt = " > "
print("hi %s, I'm the %s script" % ('Niketan', script))
print("Do you like me ?")
like = input()
print(like)
print("You said you like me Yes/No? %s" %like)