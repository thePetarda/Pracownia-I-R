import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

tempp = np.array([-4058.138169, 5658.359167, -4552.916797, -3470.000214, -5894.979656, 8037.28899])
# mocc = np.array([-1.956683333, 0.245166667, 0.427908, 0.415776, 0.322028, 0.451237333, 0.426613333])
mocc = np.array([0.236166667, 0.411788, 0.400224, 0.310041333, 0.434416, 0.410501333])
dane = np.array([tempp, mocc])
# print(dane)

T, P = dane

niepewnoscit = np.array([0.954702226, 1.331161871, 1.071099186, 0.816338308, 1.386826612, 1.890818015])
# niepewnoscip = np.array([0.003789342, 0.002461513, 0.0027579, 0.002901297, 0.002609016, 0.002983371, 0.002821285])
niepewnoscip = np.array([0.00334003, 0.003733387, 0.003930865, 0.00353621, 0.004042156, 0.003819641])
# print(niepewnosciu)

plt.xlabel("zmiana temperatury")
plt.ylabel("moc")
plt.errorbar(T, P, yerr=niepewnoscip, xerr=niepewnoscit, label='Moc', fmt='bo', capsize=0.5)

plt.show()

temp = np.array([-4058.138169, 5658.359167, -4552.916797, -3470.000214, -5894.979656, 8037.28899])
moc = np.array([0.236166667, 0.411788, 0.400224, 0.310041333, 0.434416, 0.410501333])


def line(x, a, b):
    return a * x + b


par, cov = curve_fit(line, temp, moc)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)

line = []

for elem in temp:
    line.append(par[0] * elem + par[1])


plt.plot(temp, line, 'r')
plt.show()
plt.savefig('Masa2.png')
