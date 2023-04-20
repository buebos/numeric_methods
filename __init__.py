# %%
import matplotlib.pyplot as plt
from tabulate import tabulate
from methods.bisection import bisection
import math
import numpy as np

from util.evaluate_function import evaluate_function


def function(x: float):
    return 9.81 * 68.1 / x * (1 - math.exp(-10 * x / 68.1)) - 40


xn, fxn = evaluate_function(function, 2, 22, 0.1, None)
plt.plot(xn, fxn)
plt.grid()
print(tabulate(np.transpose([xn, fxn]), ["X", "FX"], tablefmt="grid"))

print(bisection(function, 100, -10, 0.000001))
# %%
