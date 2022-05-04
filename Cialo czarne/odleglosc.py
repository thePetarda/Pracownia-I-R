import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

temp = np.array([6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76])
nap = np.array([24.03, 8.17, 4.00, 2.38, 1.59, 1.17, 0.87, 0.68, 0.56, 0.47, 0.39, 0.33, 0.27, 0.24, 0.21])

niepewnoscitemp = np.array([0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
niepewnoscinap = np.array([0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006, 0.006])

plt.xlabel("odległość [cm]")
plt.ylabel("napięcie [mV]")
plt.errorbar(temp, nap, yerr=niepewnoscinap, xerr=niepewnoscitemp, label='', fmt='bo', capsize=0.5)

plt.show()


def line(x, a):
    return a / (x ** 2)


par, cov = curve_fit(line, temp, nap)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)

line = []

for i in temp:
    line.append(par[0] / (i ** 2))


plt.plot(temp, line, 'r')
plt.show()
plt.savefig('Odleglosc.png')
