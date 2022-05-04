import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

dt = np.array([14.0, 27.5, 41.0, 55.0, 69.0, 83.5, 99.0, 112.5, 127.5, 141.0, 155.0, 169.5, 184.5, 199.5, 214.0, 228.5])
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
plt.savefig('Predkosc40.png')
