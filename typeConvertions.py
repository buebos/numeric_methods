"""
Operators
Author: Gael Herrera
"""
from tryIntConvertion import tryIntConvertion
val: str | int = ''

print('Welcome to python operators practice!\n')

while (isinstance(val, int) != True):
    val = input('Enter a string to try int convertion: ')
    val = tryIntConvertion(val)
    if isinstance(val, int) != True:
        print('\nThe input is wrong, continuing to another try...\n')
    else:
        print('The input was successfully converted to int:', str(val))
