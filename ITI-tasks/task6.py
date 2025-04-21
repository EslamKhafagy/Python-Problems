#!/bin/python3

# Write a Python program that accepts a word from the user and reverses it.

name = input("Please, Enter your name: ")

revName = []
lenName = len(name) - 1 
for i in range(len(name)):

    revName.append(name[lenName])
    lenName -= 1

print("Reversed name is \"{}\" ".format(''.join(revName)))
   
