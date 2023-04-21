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
sum: float = 0

clear()

x = float(input("Type x: "))
n = int(input("Type n: "))

for i in range(0, n + 1):
    current_result = x**i / math.factorial(i)
    sum += current_result
    table_results[0].append(i)
    table_results[1].append(sum)
    table_results[2].append(error(math.exp(x), sum))

plt.plot(table_results[0], table_results[1], color="red", linewidth=2)
plt.grid()

print(
    tabulate(
        transpose(table_results),
        ["Terms", "Experimental result", "Error percentage %"],
    )
)

# %%
