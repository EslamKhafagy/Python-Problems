#!/bin/python3

# Write a Python function to print the even numbers from a user list.

# Function to get a valid list of integers from the user
def get_integer_list():
    while True:
        try:
            user_input = input("Enter a list of integers separated by spaces: ")
            # Convert the input string into a list of integers
            integer_list = [int(x) for x in user_input.split()]
            return integer_list
        except ValueError:
            print("Invalid input. Please enter integers only.")

# Get the list from the user
sampleList = get_integer_list()

# Find even numbers
evenList = [num for num in sampleList if num % 2 == 0]

print("Even numbers in the list are: ", evenList)