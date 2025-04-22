#!/bin/python3

# Write a Python function to read a given CSV file as a dictionary. use csv.DictReader function.

import csv

dicOfData = []

with open('f1.csv', mode='r', newline='') as file:
    data = csv.DictReader(file)

    for row in data:
        dicOfData.append(row)

print(dicOfData)


