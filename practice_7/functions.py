def dummyFunction():
    """
    Prints hello world
    """
    return "Hello world"


def displayHelloFor(name: str) -> None:
    print("Hello " + name + "!")


def multiply(a: float, b: float = 2.0):
    return a * b


def square_n_cube(num: float):
    return num**2, num**3


# print("running a function:", dummyFunction())

displayHelloFor("Emi")

print(multiply(3.0))

square, cube = square_n_cube(2)
print(f'used 2 | square: {square} | cube: {cube}')
