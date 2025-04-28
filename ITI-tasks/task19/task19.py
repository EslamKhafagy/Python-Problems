#!/bin/python3

import subprocess

# Python script to create 25 file from f1 to f25.


flist = []

for i in range(24):
    n=str(i+1)
    flist.append("f"+n)


result = subprocess.Popen(["touch"] + flist, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

output, error = result.communicate()

print("Output:")
print(output)

print("Error:")
print(error)
