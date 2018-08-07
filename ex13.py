# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 20:20:19 2018

@author: niketanrane
Language Used : Python 3.6.5

"""

#ex13
from sys import argv
script, first, second, third = argv

print("The script is : ", script)
print("The first arg is:", first)
print("The second arg is:", second)
print("The third arg is : ", third)
Note : Command line arguments come as strings. So, you need to converty them accordingly whenever using. 
