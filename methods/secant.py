from typing import Callable
from matplotlib import pyplot as plt
from tabulate import tabulate
from util.Table import Table


def secant(f: Callable, max_error: float, xcur: float, xprev: float, return_root=True):
    table = Table()
    error = 100

    while error <= max_error:
        fxcur = f(xcur)
        fxprev = f(xprev)
        xnext = xcur - fxcur * (xprev - xcur) / fxprev - fxcur
        error = abs((xcur - xprev) / xcur) * 100

        if error <= max_error and return_root:
            return xcur
        else:
            table.ad_row([xprev, xcur, fxcur, xnext, error])
        

    print("--- Results ---")

    print(tabulate(table.all), ["X Previous", "X Current", "f(x)", "X Next", "Error %"])

    plt.plot(table.get_column(1), table.get_column(2))
