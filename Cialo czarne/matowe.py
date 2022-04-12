import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t = [50, 61, 70, 81, 91, 101, 111, 121]
temperatura = []

for elem in t:
    temperatura.append(elem + 273)


napięcie = np.array([0.685, 1.105, 1.475, 1.855, 2.235, 2.625, 3.095, 3.575 ])

dane = np.array([temperatura, napięcie])

temp, nap = dane

niepewnoscitemp = np.array([1, 1, 1, 1, 1, 1, 1, 1])
niepewnoscinap = np.array([0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005, 0.005])

plt.xlabel("temperatura [K]")
plt.ylabel("napięcie [mV]")
plt.errorbar(temp, nap, yerr=niepewnoscinap, xerr=niepewnoscitemp, label='', fmt='bo', capsize=0.5)

plt.show()


def line(x, a):
    return a * (x ** 4)


par, cov = curve_fit(line, temp, nap)

print(par)
perr = np.sqrt(np.diag(cov))
print(cov)
print(perr)

line = []

for i in temp:
    line.append(par[0] * (i ** 4))


plt.plot(temp, line, 'r')
plt.show()
plt.savefig('Matowe.png')
