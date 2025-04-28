#!/bin/python3

import subprocess

# python script to test connectivity to IP addr, take it from user.

ip = input("Please enter ip that you want to ping: ")

task = subprocess.run(["ping", "-c", "4", ip], capture_output=True, text=True)

print(task.stdout)

