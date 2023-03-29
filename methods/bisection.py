from typing import Callable

import numpy as np


def bisection(
    f: Callable[[float], float],
    x0: float,
    x1: float,
    offsetTol: float = 0.000001,
):
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

    iterations = 0

    while abs(fxt) > offsetTol:
        iterations += 1

        if fxt * fx1 < 0:
            x0 = xt
        elif fxt * fx1 > 0:
            x1 = xt

        xt = (x0 + x1) / 2
        fxt = f(xt)

    print("Iterations done:", iterations)

    return xt


def ecuation(x: float) -> float:
    return np.exp(-x) - x


bisection_result = bisection(ecuation, 2.0, -1.0)

print(bisection_result)
print(ecuation(bisection_result))
