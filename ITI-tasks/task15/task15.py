#!/bin/python3


# Write a function in Python to count the number of lines from a text file "file1.txt" which is not starting with an alphabet "t".

def count_lines_not_starting_with_t(file_name):
    count = 0
    # Open the file
    with open(file_name, 'r') as file:
        for line in file:
            
            line = line.strip()

            if len(line) > 0:  # Ensure the line is not empty
                first_char = line[0].lower()  # Get the first character (lowercased)
                
                # Check if the first character is not 't'
                if first_char != 't':
                    count += 1  # Increment count if line doesn't start with 't'
    
    return count

# Example:
file_name = 'f1.txt'
result = count_lines_not_starting_with_t(file_name)
print(f"Number of lines not starting with 't': {result}")

