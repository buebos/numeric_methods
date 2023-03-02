"""
Date: 2023-02-15
Author: Gael Emiliano Herrera Acuña
School: UABC
Class: 21
"""

val = input("Type a number: ")
val = int(val)

# Print examples

# Literally a sum string -> 1 + 2
print("This is a sum string, it should return the sum plain text: " + "1 + 2\n")
# The result of that sum string -> 3
print("This is an executed sum without a string, it should give out the result: " + str(1 + 2) + "\n")

# Concat prints
print("This is the value you typed in the input", str(val), "\n")
print("This is the value you typed in the input", str(val), ". This is your (value + 1) =", str(val + 1), "\n")

# This is with f strings
print(f"This is a string with f keyword displaying the value you typed: {val}\n")

name = "Gael Herrera"
age = 19
print(f"My name is: {name}. My age is: {age}")
