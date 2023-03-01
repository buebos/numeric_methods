"""
Date: 2023-02-15
Author: Gael Emiliano Herrera Acuña
School: UABC
Class: 21
"""

print("\n--- First Page ---\n")

# First page
print('The type of 5 is:', type(5))
print('The type of 3.1416 is:', type(3.1416))
print('The type of 2.0 is:', type(2.0))
print("The type of 'Hola' is:", type('Hola'))
print('The type of "Adios" is:', type("Adios"))
print('The type of 4/2 is:', type(4/2))
print('The type of True is:', type(True))
print('The type of 2+3j is:', type(2+3j))

# Second page
print("\n--- Second Page ---\n")

a=5.5
b=3
c="HOLA"
d="2.5"
f="False"
g=False
h=3.5

# Show the message with this format print("a is {type}, in integer type is:", int(a))
print("5.5 is", type(a), "in integer type is:", int(a))
print("3 is", type(b), "in float type is:", float(b))
print('"2.5" is', type(d), "in float type is:", float(d))
print("5.5 is", type(a), "in string type is:", str(a))
print("3 is", type(b), "in string type is:", str(b))
print("False is", type(g), "in string type is:", str(g))
print("3.5 is", type(h), "in complex type is:", complex(h))
# print('"False" is', type(f), "in float type is:", float(f)) # Cannot convert from string to float
# print('"HOLA" is', type(c), "in integer type is:", int(c)) # Cannot convert from string to int

# Third page
print("\n--- Third Page ---\n")

print("Is number 3 a float type? ", isinstance(3, float))
print("Is number 3 an int type? ", isinstance(3, int))
print("Is number 3 a bool type? ", isinstance(3, bool))
print("Is False a bool type? ", isinstance(False, bool))
print("Is 3+2j a complex type? ", isinstance(3+2j, complex))
print("Is True a str type? ", isinstance(True, str))
print("Is 4/3 a float type? ", isinstance(4/3, float))