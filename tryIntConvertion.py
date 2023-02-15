from ast import List


def tryIntConvertion(stringToConvert: str) -> int | None:
    convertedInt: int

    try:
        convertedInt = int(stringToConvert)
        return convertedInt
    except:
        return None