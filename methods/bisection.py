from typing import Callable

import numpy as np


def bisection(f: Callable[[float], float], x0: float, x1: float, callback: Callable | None= None, max_error=0.5):
    fx0 = f(x0)
    fx1 = f(x1)

    if fx0 * fx1 > 0:
        raise Exception(
            "The given intervals have no root in between. This would be to difficult to calculate, please give valid interval initialization, one should be greater than 0 and the other one less than 0"
        )

    if fx0 == 0:
        return x0
    elif fx1 == 0:
        return x1

    xt = (x0 + x1) / 2
    fxt = f(xt)
    xt_prev = None
    error = None

    iterations = 0

    while error == None or error > max_error:
        iterations += 1

        if xt_prev != None:
            error = abs((xt - xt_prev) / xt) * 100

        if callback:
            callback(x0, x1, xt, error, f, iterations)

        if fxt * fx1 < 0:
            x0 = xt
        elif fxt * fx1 > 0:
            x1 = xt

        xt_prev = xt
        xt = (x0 + x1) / 2
        fxt = f(xt)

    print("Iterations done:", iterations)

    return xt


def equation(x: float) -> float:
    return np.exp(-x) - x
