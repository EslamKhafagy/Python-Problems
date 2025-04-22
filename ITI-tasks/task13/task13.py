#!/bin/python3

# Write a function in Python to count uppercase character in a text file and write output to file.


with open("f1.txt", "r") as file:
    content = file.read()

sumOfUpper = 0

for char in content:
    if char.isupper():
        sumOfUpper += 1

print("Count of uppercase is: ",sumOfUpper)
