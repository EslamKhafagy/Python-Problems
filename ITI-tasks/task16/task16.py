#!/bin/python3

# Write a python function the user will enter a file name and you are required to read that file and print the number of words in it.

def wordCounter(fileName):

    word = 0
    with open(fileName, 'r') as file:
        content = file.read()
        for i in range(len(content)):
            if content[i] == ' ':
                word += 1

    return word

numOfWords = wordCounter('f1.txt')
print("Number of words is: ",numOfWords)


