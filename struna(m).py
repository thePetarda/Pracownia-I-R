import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

masa = []
for i in range(11):
    masa.append(i*0.5 + 0.75325)

dane = np.array([masa,
                [75.05, 96.15, 112.65, 128.9, 141.85, 153.9, 165.05, 175.75, 185.95, 196.45, 203.6]])
print(dane)

n, f = dane

niepewnoscin = np.array([0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
print(niepewnoscin)

plt.xlabel("masa obciążenia [kg]")
plt.ylabel("częstotliwość harmoniczna [Hz]")
plt.errorbar(n, f, yerr=niepewnoscin, label='Pomiary współczynnika $n$', fmt='bo', capsize=0.5)

plt.show()


def line(x, a):
    return a * np.sqrt(x)


par, cov = curve_fit(line, n, f)

print(par)
print(cov)
perr = np.sqrt(np.diag(cov))
print(perr)

line = []

i = 1
for elem in masa:
    line.append((par[0]*np.sqrt(elem)))
    i += 1


plt.plot(masa, line, 'r')
plt.show()
plt.savefig('Struna(m).png')
