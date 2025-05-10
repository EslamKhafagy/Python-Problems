#!/bin/python3


# Write a Python program to find those numbers which are divisible by 7 and 5, between 1500 and 2700. save output i list.

divisibleNum = []

for num in range(1500,2700):
    
    if num % 5 == 0 & num % 7 == 0:
        divisibleNum.append(num)

print(divisibleNum)


