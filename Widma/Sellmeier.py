import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# dl = np.array([656.3, 486.1, 434.5, 587.6, 667.8, 501.6, 447.1])
# wsp = np.array([1.68, 1.7, 1.72, 1.69, 1.68, 1.7, 1.71])

dl = np.array([434.5, 447.1, 486.1, 501.6, 587.6, 656.3, 667.8])
wsp = np.array([1.72, 1.71, 1.7,  1.7, 1.69,  1.68, 1.68])

niepewnosciwsp = np.array([0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03])
niepewnoscidl = np.array([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

plt.xlabel("długość fali [nm]")
plt.ylabel("współczynnik załamania")
plt.errorbar(dl, wsp, yerr=niepewnosciwsp, xerr=niepewnoscidl, label='Pomiary współczynnika $n$', fmt='bo', capsize=0.5)

plt.show()


def line(x, b, c):
    return np.sqrt((b*x**2)/(x**2 - c) + 1)


par, cov = curve_fit(line, dl, wsp)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)

line = []

for i in dl:
    line.append(np.sqrt((par[0]*i**2)/(i**2 - par[1]) + 1))


plt.plot(dl, line, 'r')
plt.show()
plt.savefig('Sellmeier.png')
