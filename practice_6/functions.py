def factorial(num: int) -> int:
    return 1 if num <= 1 else num * factorial(num - 1)


def fibonacci(
    index: int, chain: list[int] = [], position: str = "main"
) -> int:
    print(
        "Running index:",
        index,
        "| Chain:",
        chain,
        "| Position:",
        position,
        "| Returning:",
    )

    if index == 0:
        return 0
    elif index == 1:
        return 1

    chain1: list[int] = chain + [index - 1]
    chain2: list[int] = chain + [index - 2]

    return fibonacci(index - 1, chain1, "-1") + fibonacci(
        index - 2, chain2, "-2"
    )


def fibonacci_display_to(index: int) -> None:
    a: int = 1
    b: int = 1
    c: int = 0

    for i in range(index + 1):
        if i == 0:
            print(0)
        elif i == 1:
            print(1)
        else:
            a = b + c
            c = b
            b = a

            print(a)
