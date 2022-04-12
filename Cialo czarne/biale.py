import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

t = [50, 61, 70, 81, 91, 101, 111, 121]
temperatura = []

for elem in t:
    temperatura.append(elem + 273)


napięcie = np.array([3.255, 4.715, 6.365, 7.855, 9.625, 11.355, 13.175, 15.035])

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
plt.savefig('Biale.png')
