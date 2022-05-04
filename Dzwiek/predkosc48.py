import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dt = np.array([14.0, 28.0, 43.0, 57.0, 71.5, 86.5, 99.5, 114.5, 129.0, 142.5, 158.5, 172.0, 186.0, 201.0, 214.5, 230.0])
ds = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0])

# ut = np.array([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
ut = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
us = np.array([0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07, 0.07])

plt.xlabel("Odstępy czasu [μs]")
plt.ylabel("Odstępy odległości [cm]")
plt.errorbar(dt, ds, yerr=us, xerr=ut, label='Pomiary prędkości', fmt='bo', capsize=0.5)

plt.show()


def line(x, a):
    return a * x


par, cov = curve_fit(line, dt, ds)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)

line = []

for i in dt:
    line.append(par[0]*i)


plt.plot(dt, line, 'r')
plt.show()
plt.savefig('Predkosc48.png')
