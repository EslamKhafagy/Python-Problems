#!/bin/python3

# write a function to move all zero in an integer to the end 1020304050  >>>>  1234500000


ex = 1020304050

zerosToEnd = []
numOfZeros = 0

intToStr = str(ex)

for i in range(len(intToStr)):
    if intToStr[i] != '0':
        zerosToEnd.append(intToStr[i])
        numOfZeros += 1

for i in range(numOfZeros):
    zerosToEnd.append('0')


ans = int("".join(zerosToEnd))

print(ans)

