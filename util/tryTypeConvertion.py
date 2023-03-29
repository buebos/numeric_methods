# Converts a string to integer or returns null if error
from typing import Callable


def tryTypeConvertion(stringToConvert: str, typeTo: Callable) -> int | None:
    convertedInt: int

    try:
        convertedInt = typeTo(stringToConvert)
        return convertedInt
    except:
        return None