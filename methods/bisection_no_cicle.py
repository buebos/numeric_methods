import math


def f(x: float):
    return 9.81 * 68.1 / x * (1 - math.exp(-10 * x / 68.1)) - 40


def eap(xr: float, xr_prev: float):
    return abs((xr - xr_prev) / xr) * 100


def help_this_function_is_so_long():
    xi = float(input("Type the inferior limit: "))
    xs = float(input("Type the superior limit: "))
    digits = float(input("Type the significative digits: "))
    es = 0.5 * 10 ** (2 - digits)
    print("Error criteria is:", es)

    xr_prev = None
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = None

    print("# 1")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 2")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 3")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return
    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 4")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 5")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 6")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 7")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 8")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 9")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 10")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 11")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 12")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 13")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 14")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 15")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 16")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 17")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 18")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 19")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 20")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 21")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 22")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 23")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 24")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 25")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    if fxr * fxs < 0:
        xi = xr
    elif fxr * fxs > 0:
        xs = xr

    xr_prev = xr
    xr = (xi + xs) / 2
    fxi = f(xi)
    fxs = f(xs)
    fxr = f(xr)
    Eap = round(eap(xr, xr_prev), 4)

    print("# 26")
    print("xi =", xi)
    print("xs =", xs)
    print("xr =", xr)
    print("fxi =", fxi)
    print("fxs =", fxs)
    print("fxr =", fxr)
    print("Eap =", Eap)

    if Eap < es:
        print("----- Se ha alcanzado el error deseado -----")
        return

    print("There aren't enought iterations written for the error you want, PLEASE USE A LOOP!!!!")


help_this_function_is_so_long()
