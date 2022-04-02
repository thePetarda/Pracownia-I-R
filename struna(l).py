import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dlugosc = np.array([30, 40, 50, 60, 70])
dane = np.array([dlugosc,
                [529.6, 398.1, 319.3, 267.2, 229.6]])
print(dane)

n, f = dane

niepewnoscin = np.array([0.7, 0.7, 0.7, 0.7, 0.7])
print(niepewnoscin)

plt.xlabel("długość struny [cm]")
plt.ylabel("częstotliwość harmoniczna [Hz]")
plt.errorbar(n, f, yerr=niepewnoscin, label='Pomiary współczynnika $n$', fmt='bo', capsize=0.5)

plt.show()


def line(x, a, b):
    return (a / x) + b


par, cov = curve_fit(line, n, f)

print(par)
print(cov)
perr = np.sqrt(np.diag(cov))
print(perr)

line = []
dl = []

i = 30
while i <=70:
    dl.append(i)
    line.append(par[0]/i+par[1])
    i+=1


plt.plot(dl, line, 'r')
plt.show()
plt.savefig('Struna(l).png')
