import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dane = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                [204, 409, 613.5, 818.1, 1022.5, 1227.1, 1431.8, 1636.2, 1841.9, 2039.4]])
print(dane)

n, f = dane

niepewnoscin = np.array([0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
print(niepewnoscin)

plt.xlabel("liczba harmoniczna")
plt.ylabel("częstotliwość harmoniczna [Hz]")
plt.errorbar(n, f, yerr=niepewnoscin, label='Pomiary współczynnika $n$', fmt='bo', capsize=0.5)

plt.show()


def line(x, a, b):
    return a * x + b


par, cov = curve_fit(line, n, f)

print(par)
perr = np.sqrt(np.diag(cov))
print(cov)
print(perr)

line = []

for i in range(11):
    line.append(par[0]*i+par[1])


plt.plot(line, 'r')
plt.show()
plt.savefig('Struna(n).png')
