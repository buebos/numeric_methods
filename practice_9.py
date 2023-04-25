# %%
import math
from matplotlib import pyplot as plt
from tabulate import tabulate
from util.clear import clear
from util.transpose import transpose


def error(real: float, experimental: float):
    return abs((real - experimental) / real) * 100


# [0]: 'number_of_terms'
# [1]: 'experimental_result'
# [2]: 'error_percentage'
table_results = [[], [], []]

clear()

xi = float(input("Type x inferior: "))
xs = float(input("Type x superior: "))
while xi > xs:
    xs = float(input("Type x superior again, be sure to not type a number greater than the x inferior: "))

step = float(input("Type the step between each x iteration: "))
while step < 0:
    step = float(input("Step must be a number greater than 0, type it again please: "))

x = xi
n = int(input("Type n: "))

while x <= xs:
    ex: float = 0
    for i in range(0, n + 1):
        current_result = x**i / math.factorial(i)
        ex += current_result
    table_results[0].append(x)
    table_results[1].append(ex)
    table_results[2].append(error(math.exp(x), ex))   
    x += step


plt.plot(table_results[0], table_results[1], color="red", linewidth=2)
plt.grid()

print(tabulate(transpose(table_results), ["Exponential", "Experimental result", "Error percentage %"]))

x = int(input("Type x to raise Euler: "))
n = int(input("Type n: "))
sum_ex = 0
results_2 = [[], [], []]

for i in range(n + 1):
    current_result = x**i / math.factorial(i)
    sum_ex += current_result
    results_2[0].append(i)
    results_2[1].append(sum_ex)
    results_2[2].append(error(math.exp(x), sum_ex))


print(tabulate(transpose(results_2), ["Terms", "Sum with term amount", "Error percentage %"]))

# %%
