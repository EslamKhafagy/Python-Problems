#!/bin/python3


# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
 
dic1={1: 10, 2: 20}
dic2={3: 30, 4: 40}
dic3={5: 50, 6: 60}

# expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

conDictionary = {}

for dic in (dic1, dic2, dic3):
    for key in dic:
        if key not in conDictionary:
            conDictionary[key] = dic[key]

print(conDictionary)
