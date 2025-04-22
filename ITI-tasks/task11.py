#!/bin/python3


# Write a Python function to calculate the factorial of a number.


num = int(input("Enter the number, for calculating factorial: "))
n = num
fact = 1

while num != 0:
    fact *= num
    num -= 1


print("The factorial of a number {} is: {}".format(n,fact))

