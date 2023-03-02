from util.tryTypeConvertion import tryTypeConvertion


def persistInputType(inputMessage: str, errorMessage: str, typeDesired: int | float | complex) -> int:
    val: str = ""
    while isinstance(val, typeDesired) != True:
        val = input(inputMessage)
        val = tryTypeConvertion(val, typeDesired)

        if isinstance(val, typeDesired) != True:
            print(f"\n{errorMessage}\n")
        else:
            return val
