# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:15:07 2018

@author: niketan
"""

#ex10
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\n a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list: 
\t* Cat food 
\t* Fishies 
\t* Catnip\n\t* Grass"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

'''
while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" %i)
'''

print("%r" %('\\')) # will print '\\' -> As given 
print("%s" %('\\')) # will print '\' -> The way you want to 
