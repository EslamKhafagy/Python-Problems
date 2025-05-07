#!/bin/python3

# Write a Python program to get the largest number from a list.

# Take the list from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
setList = [int(x) for x in user_input.split()]

largestNum = setList[0]

for num in setList:
    if num > largestNum:
        largestNum = num

print("The largest number from the list is {}".format(largestNum))