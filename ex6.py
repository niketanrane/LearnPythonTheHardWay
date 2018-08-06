# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:13:57 2018

@author: niketan
"""

#ex6
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)
print(x)
print(y)

print("I said: %r " %x)
print("I also said '%s'" %y)

hilarious= False
joke_eval = "Isn't that joke so funny?! %r"
print(joke_eval % hilarious)

w = "This is left side of ..."
e = "a string with right side"
print(w+e)