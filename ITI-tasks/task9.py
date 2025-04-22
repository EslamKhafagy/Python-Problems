#!/bin/python3

# Write a Python program to map two lists into a dictionary

list1 = ["name", "age", "city"]

list2 = ["mohamed", 30, "cairo"]


l2Dict = {}

i=0
for i in range(len(list2)):
    l2Dict[list1[i]] = list2[i]

print(l2Dict)

