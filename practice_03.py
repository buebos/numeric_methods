from util.persistInput import persistInputType
import math

errorMessage: str = "The input you typed is wrong, make sure to only use numbers"

base: float = persistInputType("Type the base of the triangle: ", errorMessage, float)
height: float = persistInputType(f"Base is {base}, put the height in: ", errorMessage, float)
area: float = round(base * height / 2, 2)
perimeter: float = math.sqrt(height**2 + (base / 2) ** 2) * 2 + base

print(f'{"="*30}\n\tArea | Perimeter\n{"="*30}\n\t{area}  | {perimeter:.3f}'.format(permiter=perimeter))
