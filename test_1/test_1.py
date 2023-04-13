def taylor_series(n: int, x: int):
    sum: float = 1

    for i in range(1, n):
        factorial: int = 1

        for j in range(1, i + 1):
            factorial = factorial * j
        sum += x**i / factorial

    return sum


print("1er termino: ", taylor_series(1, 1))
print("2do termino: ", taylor_series(2, 1))
print("3er termino: ", taylor_series(3, 1))
print("4to termino: ", taylor_series(4, 1))

factorial_cache = 1


def taylor_series_cached(n: int, x: int):
    global factorial_cache
    factorial_cache = 1

    sum: float = 1

    for i in range(1, n):
        factorial_cache = factorial_cache * i

        sum += x**i / factorial_cache

    return sum


print("1er termino: ", taylor_series_cached(1, 1))
print("2do termino: ", taylor_series_cached(2, 1))
print("3er termino: ", taylor_series_cached(3, 1))
print("4to termino: ", taylor_series_cached(4, 1))
