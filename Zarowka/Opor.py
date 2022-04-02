import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

napiecie = np.array([0.21, 0.41, 0.61, 0.81, 1.01, 1.21, 1.41, 1.61, 1.81, 2.01, 2.21, 2.41, 2.61])
natezenie = np.array([17.7, 34.9, 52.1, 69.5, 86.8, 104.2, 121.5, 138.9, 156.3, 173.8, 191.3, 209.1, 226.8])
dane = np.array([napiecie, natezenie])
# print(dane)

u, i = dane

niepewnosciu = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
niepewnoscii = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])
# print(niepewnosciu)

plt.xlabel("natężenie [mA]")
plt.ylabel("napięcie [V]")
plt.errorbar(i, u, yerr=niepewnosciu, xerr=niepewnoscii, label='Pomiary współczynnika $n$', fmt='bo', capsize=0.5)

plt.show()


def line(x, a):
    return a * x


par, cov = curve_fit(line, i, u)

print(par*1000)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr*1000)

line = []

for elem in natezenie:
    line.append(par[0] * elem)


plt.plot(natezenie, line, 'r')
plt.show()
plt.savefig('OpórR.png')
