# Comenzamos con un input
userStr: str = input("Introduce cualquier tipo de texto: ")
# Convertimos a minúsculas para evitar comparar las vocales en su
# versión minúscula y mayúscula. Cabe decir que no se usará esto para
# determinar si la vocal era mayúscula o minúscula pues ya no sería el texto
# original; si el usuario escribió "A" se convertirá a "a". Por lo tanto,
# utilizaremos tanto lo que escribió originalmente como lo que procesamos para
# obtener los resultados. Si no se entiende, es explicará más adelante en 
# los comentarios de este script o.O
userProcessedStr: str = userStr.lower()
# Obtenemos la longitud del texto introducido
strLength: int = len(userStr)

# Imprimimos la longitud del texto independientemente de lo que
# se haya introducido
print(f"La longitud del texto ingresado es: {strLength}")

# Si la longitud del texto es de una letra verificamos que sea una vocal
if strLength == 1:
    # Aquí se usa lo que comentaba al inicio, el input convertido a lower,
    # ya que de momento no nos interesa si fue una vocal mayúscula o minúscula
    # solo nos interesa saber si y solo si fue una vocal. Comparamos con cada una
    # de las vocales. Nota: utilizamos la variable userProcessedStr (dato 
    # procesado de usuario)
    if (
        userProcessedStr == "a"
        or userProcessedStr == "e"
        or userProcessedStr == "i"
        or userProcessedStr == "o"
        or userProcessedStr == "u"
    ):
        # En este if, si que usariamos la entrada de texto original, ya que
        # ahora si nos interesa saber si fue minúscula o mayúscula. En este caso
        # no hay necesidad de poner una expresión lógica como el "==" ya que
        # ejecutar islower() por si mismo como condición, significa que 
        # el valor de eso será True o False, y al evaluar el if, digamos que el 
        # programa no leerá .islower(); leerá lo que vale: True o False dependiendo
        # si la letra si era minúscula. De otra manera, si no es minúscula, significa
        # que es mayúscula, por eso no hay necesidad de verificar y solo ponemos un
        # else
        if userStr.islower():
            print("Tu texto es una vocal en minúscula")
        else:
            print("Tu texto es una vocal en mayúscula")
    # Si no fue una vocal, imprimimos el mensaje que corresponda
    else:
        print("Tu texto no es una vocal")
else:
    print("Tu texto tiene más de 1 caracter")
