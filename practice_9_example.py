#%%
import math
from matplotlib import pyplot as plt
from tabulate import tabulate
import os


# Definición de función para calcular el error porcentual
def error(real: float, experimental: float):
    return abs((real - experimental) / real) * 100


# Inicialización de variables
t1 = []
t2 = []
graphi = []
graphfx = []
sum_ex = 0
graph_sum_ex = []

# Limpieza de la consola
os.system("cls")

# Entrada de datos por el usuario
xi = float(input("Type x inferior: "))
xs = float(input("Type x superior: "))

# Verificación de que xs es mayor o igual que xi
while xi > xs:
    xs = float(
        input(
            "Type x superior again, be sure to not type a number greater than the x inferior: "
        )
    )

step = float(input("Type the step between each x iteration: "))

# Verificación de que el valor de step es mayor que 0
while step < 0:
    step = float(
        input(
            "Step must be a number greater than 0, type it again please: "
        )
    )

x = xi
n = int(input("Type n: "))

# Cálculo de la función exponencial de Euler para cada valor de x en el rango dado
while x <= xs:
    ex: float = 0
    for i in range(0, n + 1):
        current_result = x**i / math.factorial(i)
        ex += current_result
    current_error = error(math.exp(x), ex)

    # Agregar los resultados a una tabla y a listas para la gráfica
    t1.append([x, ex, current_error])
    graphi.append(x)
    graphfx.append(ex)

    x += step

# Graficar los resultados obtenidos
plt.plot(graphi, graphfx, color="red", linewidth=2)
plt.grid()

# Imprimir los resultados obtenidos en la tabla
print(f"--- Euler raised from {xi} to {xs} ---")
print(
    tabulate(
        t1,
        ["Exponential", "Experimental result", "Error percentage %"],
    )
)

# Nueva entrada de datos por el usuario
x = int(input("Type x to raise Euler: "))
n = int(input("Type n: "))

# Cálculo de la función exponencial de Euler sumando n términos
for i in range(n + 1):
    current_result = x**i / math.factorial(i)
    sum_ex = current_result + sum_ex

    # Agregar los resultados a una tabla
    t2.append([i, sum_ex, error(math.exp(x), sum_ex)])

# Imprimir los resultados obtenidos en la tabla
print(f"--- Euler raised to {x} ---")
print(
    tabulate(
        t2,
        ["Terms", "Sum with term amount", "Error percentage %"],
    )
)

# %%
