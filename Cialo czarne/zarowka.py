import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

temp = np.array([602.11, 879.99, 1096.70, 1259.72, 1404.21, 1519.32, 1623.92, 1722.72, 1804.86, 1893.68, 1965.66, 2038.62, 2105.23, 2166.30, 2230.46, 2290.16, 2345.85, 2397.94, 2446.76, 2500.30])
nap = np.array([0, 0.11, 0.45, 0.98, 1.68, 2.54, 3.50, 4.65, 5.88, 7.15, 8.48, 9.91, 11.49, 13.08, 14.64, 16.39, 17.75, 19.75, 21.71, 23.74])

niepewnoscitemp = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
niepewnoscinap = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])

plt.xlabel("temperatura [K]")
plt.ylabel("napięcie [mV]")
plt.errorbar(temp, nap, yerr=niepewnoscinap, xerr=niepewnoscitemp, label='', fmt='bo', capsize=0.5)

plt.show()


def line(x, a, b):
    return a * (x ** 4) + b


par, cov = curve_fit(line, temp, nap)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)

line = []

for i in temp:
    line.append(par[0] * (i ** 4) + par[1])


plt.plot(temp, line, 'r')
plt.show()
plt.savefig('Zarowka.png')
