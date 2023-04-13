def arrays():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    reversed_array = array[::-1]
    sum_vec = [array[i - 1] + reversed_array[i - 1] for i in reversed_array]

    print("sum:", sum_vec)

    print("reversed:", reversed_array)


def questions():
    array = []
    run = True

    while run:
        element = input("Enter the element new array element: ")

        array.append(element)

        run = input("Continue? (y/n): ") == "y"

    print("array:", array)
    print("length:", len(array))


def replace(phrase: str, to_replace: str, replacement: str = ""):
    phrase_list = list(phrase)

    for i in range(len(phrase)):
        if phrase_list[i] == to_replace:
            phrase_list[i] = replacement

    return "".join(phrase_list)


print(replace(input("Phrase: "), input("Character to replace: "), input("Character replacement: ")))
