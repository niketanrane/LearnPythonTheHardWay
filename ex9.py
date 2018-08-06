# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:14:46 2018

@author: niketan
"""

#ex9
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJune\nJuly\nAug"
print("here are the days", days)
print(f"here are the months", months)
print(" " "There is something going on here.\nWith the three double-quotes.\nWe'll be able to type as much as we like.\
\Even 4 lines, or 5" " ")
print(f"%r" %(months)) # tip : %r does not take into account '\n' characters 
