#!/bin/python3


# Write a Python program to get the largest number from a list.--> [3,7,10,18,20,70,3,16,9]



setList = [3,7,10,18,20,70,3,16,9]

largestNum = setList[0]

for num in setList:
    if num > largestNum:
        largestNum = num

print("The largest number from a list is {}".format(largestNum))

        
