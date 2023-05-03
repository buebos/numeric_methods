# %%
import math

import matplotlib.pyplot as plt
from tabulate import tabulate

from methods.bisection import bisection
from util.evaluate_function import evaluate_function
from util.transpose import transpose


def function(x: float):
    return 9.81 * 68.1 / x * (1 - math.exp(-10 * x / 68.1)) - 40


def scarborough(digits: float):
    return 0.5 * 10 ** (2 - digits)


xi = float(
    input("Type the initial inferior limit for bisection method (x0): ")
)
xs = float(
    input("Type the initial inferior limit for bisection method (x1): ")
)
max_error = scarborough(float(input("Type the significant digits: ")))
xn, fxn = evaluate_function(function, 2, 22, 0.1, None)
table = []


def callback(xi, xs, xr, error, f, iterations):
    table.append(
        [
            iterations,
            xi,
            xs,
            xr,
            f(xi),
            f(xs),
            f(xr),
            round(error, len(str(max_error))) if error else None,
        ]
    )


bisection(function, xi, xs, callback, max_error=max_error)

print(
    tabulate(
        table,
        ["iteration", "xi", "xs", "xr", "fxi", "fxs", "fxr", "error"],
        tablefmt="grid",
    )
)

plt.plot(xn, fxn)
plt.grid()

# %%
