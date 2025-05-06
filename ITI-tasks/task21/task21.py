#!/bin/python3

#--------------------------------------------------------------------------------------------------#
# Python Module Challenge:
# 1. Create a script that finds and displays prime numbers from 1 to 250
# 2. Save the found prime numbers to results.txt file
# 3. Test and validate the results in the output file
# 4. Save the script and make a note of its location (absolute path) for future reference.
#--------------------------------------------------------------------------------------------------#

# Here we check if the file exists and if it does, we delete it
def check_results_file():
    import subprocess
    # Check if file exists using ls command
    check_process = subprocess.Popen(['ls', 'results.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    check_process.communicate()
    
    if check_process.returncode == 0:  # File exists
        # Delete the file using rm command
        delete_process = subprocess.Popen(['rm', 'results.txt'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        delete_process.wait()
        print("\nExisting results.txt file was found and removed\n")
    else:
        print("\nNo existing results.txt file found, proceeding with new file creation\n")


# Here we create a list to store the prime numbers
prime_list = []
# Here we define a function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
# Here we define a function to append prime numbers to the list
def append_prime_to_list(start, end):
    print(f"Prime numbers between {start} and {end} are stored at file called results.txt \n")
    for num in range(start, end + 1):
        if is_prime(num):
            prime_list.append(num)
# Here we ask the user for the range of numbers to check for primes
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

# Here we call the function to check if the file exists and if it does, we delete it
check_results_file()

# Here we call the function to append prime numbers to the list
append_prime_to_list(start, end)                        

# Here we create a file called result.txt to store primes to it
with open("results.txt", "w") as f:
    for num in prime_list:
        f.write(str(num) + " ")

# Here we read the file to check if it worked
print("We read results.txt using open function in read mode to check it")
with open("results.txt", "r") as f:
    print(f.read())