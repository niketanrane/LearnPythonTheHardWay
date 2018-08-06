# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:14:32 2018

@author: niketan
"""

#ex8
formatter = "%r %r %r %r"
print(formatter % (1,2,3,4))
print(formatter % ("One", "Two", "Three", "Four"))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % ("I had thins thing", "That you could type up right.", "But it didn't sing", "So, I said goodnight "))