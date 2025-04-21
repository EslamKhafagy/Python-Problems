#!/bin/python3


# Write a Python program to remove duplicates from a list. --> [2,7,2,10,7,15]

taskList = [2,7,2,10,7,15]

special = []

for i in range(len(taskList)):

    isDouplicated = False

    for j in range(len(special)):

        if taskList[i] == special[j]:
            isDouplicated = True
            break

    if not isDouplicated:
        special.append(taskList[i])

print(special)
