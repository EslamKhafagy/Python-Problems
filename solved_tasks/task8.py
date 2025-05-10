#!/bin/python3

# Write a Python program to sum all the items in a dictionary.

# Function to get a dictionary from the user
def get_user_dict():
    user_dict = {}
    print("Enter key-value pairs for the dictionary (type 'done' to finish):")
    while True:
        key = input("Enter key (or 'done' to stop): ")
        if key.lower() == 'done':
            break
        try:
            value = int(input(f"Enter value for key '{key}': "))
            user_dict[key] = value
        except ValueError:
            print("Invalid value. Please enter an integer.")
    return user_dict

# Get the dictionary from the user
myDict = get_user_dict()

# Calculate the sum of all values in the dictionary
total_sum = sum(myDict.values())

print("The sum of all items in the dictionary is:", total_sum)