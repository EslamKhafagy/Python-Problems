#!/bin/python3

# 2- Write a Python program to sum all the items in a list.

# Take the list from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
myFirstList = [int(x) for x in user_input.split()]

listSum = 0

for num in myFirstList:
    listSum += num

print("Sum of list is: ", listSum)