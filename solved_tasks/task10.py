#!/bin/python3

# Write a Python function to find the maximum of three numbers.

# create empty list 
myList = [0] * 3
num = ["1st", "2nd", "3rd"]

# for loop to input numbers
for i in range(len(myList)):
    while True:
        try:
            myList[i] = int(input("Enter your {} number: ".format(num[i])))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid input. Please enter an integer.")

maxNum = myList[0]

for i in range(len(myList)):
    if maxNum < myList[i]:
        maxNum = myList[i]

print("The maximum of three numbers is: ", maxNum)