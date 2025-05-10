#!/bin/python3

# Write a function to move all zeros in an integer to the end
# Example: 1020304050  >>>>  1234500000

# Take input from the user
ex = int(input("Enter a number that contains zeros: "))

zerosToEnd = []
numOfZeros = 0

intToStr = str(ex)

for i in range(len(intToStr)):
    if intToStr[i] != '0':
        zerosToEnd.append(intToStr[i])
    else:
        numOfZeros += 1

for i in range(numOfZeros):
    zerosToEnd.append('0')

ans = int("".join(zerosToEnd))

print("Result:", ans)