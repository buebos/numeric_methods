userStr: str = input("Introduce cualquier tipo de texto: ")
userProcessedStr = userStr.lower()
strLength: int = len(userStr)

print(f"La longitud del texto ingresado es: {strLength}")

if strLength == 1:
    if (
        userProcessedStr == "a"
        or userProcessedStr == "e"
        or userProcessedStr == "i"
        or userProcessedStr == "o"
        or userProcessedStr == "u"
    ):
        if userStr.islower() == True:
            print("Tu texto es una vocal en minúscula")
        else:
            print("Tu texto es una vocal en mayúscula")
    else:
        print("Tu texto no es una vocal")
else:
    print("Tu texto tiene más de 1 caracter")
