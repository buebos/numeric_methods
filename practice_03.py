from util.persistInput import persistInput
import math

errorMessage: str = 'The input you typed is wrong, make sure to only use numbers'

base: float = persistInput(
    'Type the base of the triangle: ', errorMessage, float)
height: float = persistInput(
    f'Base is {base}, put the height in: ', errorMessage, float)
area: float = round(base * height / 2, 2)
permiter: float = round(math.sqrt(height**2 + (base / 2)**2) * 2 + base, 3)

print(f'{"="*30}\n\tArea | Perimeter\n{"="*30}\n\t{area}  | {permiter}')
