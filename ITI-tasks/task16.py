#!/bin/python3

import subprocess

# Check if you have an account with name ITI in your machine.

user = input("Please Enter user to want to search for: ")

task = subprocess.Popen(["id",user], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)

output,error = task.communicate()

if output:
    print("User exist")
else:
    print("User doesn't exist")
