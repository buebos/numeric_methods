def general_formula_for(a: float, b: float, c: float):
    """
    Returns the two x found for the given parameters
    """
    sqrt = ((b**2) - (4 * a * c)) ** 0.5
    below = 2 * a

    return (-b + sqrt) / below, (-b - sqrt) / below


def display_multiply(num: int):
    """
    Returns multiply table of num in one row
    """
    for i in range(1, 11):
        print(f"{num * i}", end=" ")

    print()


def labelBy2Div(num: int):
    """
    Labels a number for when it's even, odd or zero
    """
    if num == 0:
        return "zero"
    elif num % 2 == 0:
        return "even"
    else:
        return "odd"

run = True

while run:
    """
    Runs the whole program
    """

    print("=" * 30 + " Menu " + "=" * 30)
    print("\n1. General formula\n")
    print("2. Multiply Table\n")
    print("3. Even, odd or zero\n")
    print("=" * 66)

    user_selection = int(input("Enter only the number please: "))

    while user_selection < 1 or user_selection > 3:
        user_selection = int(input("Enter only numbers from 1 to 3 please: "))

    if user_selection == 1:
        a = float(input("Enter the expression a: "))
        b = float(input("Enter the expression b: "))
        c = float(input("Enter the expression c: "))

        x1, x2 = general_formula_for(a, b, c)

        print(f"x1 is: {x1} | x2 is: {x2}")
    elif user_selection == 2:
        num = int(input("Enter the number to compute the multiply table (integer only): "))

        display_multiply(num)
    else:
        num = int(input("Enter the integer to check if it's even, odd or zero: "))

        print(f"Is {labelBy2Div(num)}")

    run = input("Do you want to return to menu to do another function? (y/n): ") == "y"

print(f"\n{'='*20} | Bye bye | {'='*20}\n")
