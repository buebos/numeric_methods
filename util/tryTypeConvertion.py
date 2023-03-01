# Converts a string to integer or returns null if error
def tryTypeConvertion(stringToConvert: str, typeTo: int | float | complex) -> int | None:
    convertedInt: int

    try:
        convertedInt = typeTo(stringToConvert)
        return convertedInt
    except:
        return None