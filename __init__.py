# %%

import math
from tabulate import tabulate
from matplotlib import pyplot as plt
from util.clear import clear

clear()

x = float(input("Type x for the taylor series: "))
n = int(input("Type n for the amount of terms: "))
table_results = []
xn = []
fxn = []
sum: float = 0


def error(real: float, experimental: float):
    return round(abs((real - experimental) / real) * 100, 2)


def calc_error_of_taylor(iterations: int, fx: float, x: float):
    table_results.append([iterations, fx, error(math.exp(x), fx)])
    xn.append(iterations)
    fxn.append(fx)


for i in range(0, n):
    current_term = x**i / math.factorial(i)
    sum += round(current_term, 4)
    calc_error_of_taylor(i + 1, sum, x)

plt.plot(xn, fxn, color="red", linewidth=2)
plt.grid()

print(
    tabulate(
        table_results,
        ["Amount of terms", "Experimental result", "Error percentage (%)"],
        tablefmt="grid",
    )
)

# %%
