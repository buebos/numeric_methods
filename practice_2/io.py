import sys

sys.path.append("../python")
from util.persistInput import persistInput

side: int = persistInput("Type the size of a square to find it's area and perimeter: ", int)
print(f"The perimeter of the square is: {side*4}. The area is: {side**2}.")
