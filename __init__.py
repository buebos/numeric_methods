# %%

import math
from tabulate import tabulate
from matplotlib import pyplot as plt
from util.clear import clear

clear()

x = float(input("Type x: "))
n = int(input("Type n: "))
table_results = []
xn = []
fxn = []
sum: float = 0


def error(real: float, experimental: float):
    return abs((real - experimental) / real) * 100


def calc_error_of_taylor(iterations: int, fx: float, x: float):
    table_results.append([iterations, fx, error(math.exp(x), fx)])
    xn.append(iterations)
    fxn.append(fx)


for i in range(0, n):
    current_result = x**i / math.factorial(i)
    sum += current_result
    calc_error_of_taylor(i + 1, sum, x)

plt.plot(xn, fxn, color="red", linewidth=2)
plt.grid()

print(tabulate(table_results, ["iterations", "experimental result", "error percentage"]))

# %%
