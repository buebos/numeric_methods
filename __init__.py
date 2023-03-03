import re


def cut_sentence(line: str, maxLen: int) -> str:
    words = re.findall(r"[a-z|A-Z]*\w", line)
    outStr = ""

    for word in words:
        if len(outStr + word) > maxLen:
            return outStr[:-1] + "..."
        else:
            outStr += word + ' '

    return line


print("Example:")
print(cut_sentence("Hi my name is Alex", 8))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
