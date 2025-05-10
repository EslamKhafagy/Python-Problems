#!/bin/python3

# Write a Python program to remove duplicates from a list.

# Take the list from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input string into a list of integers
taskList = [int(x) for x in user_input.split()]

special = []

for i in range(len(taskList)):

    isDouplicated = False

    for j in range(len(special)):

        if taskList[i] == special[j]:
            isDouplicated = True
            break

    if not isDouplicated:
        special.append(taskList[i])

print("List after removing duplicates:", special)