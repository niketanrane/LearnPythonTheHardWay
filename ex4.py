# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:13:08 2018

@author: niketan
"""

#ex4 
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
avg_pas_per_car = passengers/cars_driven
print("There are", cars, "cars available")
print("There are", drivers, "Available.")
print("There will be", cars_not_driven, "empty cars today")
print("We have trasport", carpool_capacity, "today")
print("We have", passengers, "to carpool today")
print("We need to put about", avg_pas_per_car, "in each car")