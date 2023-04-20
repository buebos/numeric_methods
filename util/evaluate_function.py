from typing import Callable

def evaluate_function(
    fn: Callable[[float], float],
    xi: float,
    xu: float,
    step: float,
    # For every iteration calculated
    callback: Callable[[float, float], None] | None,
):
    if xi > xu:
        return [], []

    i = xi
    xn = []
    fxn = []

    while i <= xu:
        curent_result = fn(i)
        xn.append(i)
        fxn.append(curent_result)

        if callback:
            callback(i, curent_result)

        i += step

    return xn, fxn