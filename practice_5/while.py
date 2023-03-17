# %% First exercise

i = 4

while i < 8:
    print(i)
    i += 1

i = 1

while i < 10:
    print(i, end=" ")
    i += 2

print(f"\nValor final de i: {i}")

# %% Second exercise

first = input("Escribe una letra clave: ")
second = input("Ingresa nuevamente la letra clave: ")
tries = 0

while first != second:
    second = input("No es correcta, ingresala nuevamente: ")
    tries += 1

print(f"La letra clave es: {first}. Fallaste: {tries} veces")

# %% Third exercise

stop = False

while not stop:
    n = int(input("Introduce un valor para generar la tabla de multiplicar: "))
    i = 1

    while i <= 12:
        print(f"{n} * {i} = {n * i}")
        i += 1

    toContinue = input("Deseas continuar? n para no / cualquier otra letra para si: ").lower()
    stop = toContinue == "n"

# %% Fourth exercise

n = int(input("Ingresa la cantidad de numeros que quieres ingresar: "))
maxNum = None
i = 1

while i <= n:
    num = int(input("Introduce el numero: "))

    if not maxNum or maxNum < num:
        maxNum = num

    i += 1

print(f"El numero mayor detectado fue: {maxNum}")

# %%
