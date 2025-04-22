#!/bin/python3

# Write a Python program to sum all the items in a dictionary.

myDict = {'data1': 100, 'data2': -54, 'data3': 247}

sum = 0

for key in myDict:

    sum += myDict[key]


print(sum)

