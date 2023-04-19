from typing import Callable
import matplotlib.pyplot as plt

def graph(
    fn: Callable[[float], float],
    xi: float,
    xu: float,
    step: float,
    callback: Callable[[float, float], None] | None,
    run_plot: bool = False,
    line_color="black",
    line_width=2.0,
):
    if xi > xu:
        return

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

    if run_plot:
        plt.plot(xn, fxn, color=line_color, linewidth=line_width)
        plt.grid()

    return xn, fxn
