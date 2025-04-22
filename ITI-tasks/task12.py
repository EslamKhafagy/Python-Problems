#!/bin/python3


# Write a Python function to print the even numbers from a given list.

sampleList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Expected Result : [2, 4, 6, 8]


evenList = []

for i in range(len(sampleList)):
    if sampleList[i] % 2 == 0:
        evenList.append(sampleList[i])

print("Even number at the list is: ", evenList)

