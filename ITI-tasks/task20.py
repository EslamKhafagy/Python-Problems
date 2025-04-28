#!/bin/python3

import subprocess

# Check if you have an account with name ITI in your machine.

user = input("Please Enter user tou want to search")

process = subprocess.Popen(["cat", "/etc/passwd" , "|", "grep", user], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()  
    if process.returncode == 0:
        print(f"User '{username}' exists on the system.")
        print(output)  
    else:
        print(f"User '{username}' does not exist.")
        print(error)  
except Exception as e:
    print(f"Error: {e}")
