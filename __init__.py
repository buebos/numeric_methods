# %%
from matplotlib import pyplot as plt

n = int(input("n: "))
x = []
y = []
sumx = 0
sumy = 0
sumx2 = 0
sumxy = 0
xavrg = 0
yavrg = 0


for i in range(n):
    xi = float(input(f"x{i}: "))
    yi = float(input(f"y{i}: "))

    x.append(xi)
    y.append(yi)
    sumx += x[i]
    sumy += y[i]
    sumx2 += (x[i]) ** 2
    sumxy += x[i] * y[i]

xavrg = sumx / n
yavrg = sumy / n

print(f"sumx {sumx}")
print(f"sumy {sumy}")
print(f"sumx2 {sumx2}")
print(f"sumx**2 {sumx**2}")
print(f"sumxy {sumxy}")
print(f"xavrg {xavrg}")
print(f"yavrg {yavrg}")

m = ((n * sumxy) - (sumx * sumy)) / (n * sumx2 - (sumx**2))
b = (sumy - (m * sumx)) / n

print(f"m is {m}")
print(f"b is {b}")
print(f"Linear equation is: y = {m}x + {b}")
print(f"5 evaluated in equation is {m*5 + b}")

plt.scatter(x, y)
plt.grid()

# %%
