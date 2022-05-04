import numpy as np
import xlrd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Give the location of the file
loc = ("Kabel.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

data = []
udata = []

i = 33
while (i < 47):
    # print(int(sheet.cell_value(i, 2)))
    data.append([float(sheet.cell_value(i, 0)), float(sheet.cell_value(i, 1))])
    udata.append([0.01, 0.05])
    i += 1

data.sort(key=lambda tup: tup[1])

odl = []
czas = []
for el in data:
    odl.append(el[0])
    czas.append(el[1])

uodl = []
uczas = []
for el in udata:
    uodl.append(el[0])
    uczas.append(el[1])

plt.xlabel("opór [MΩ]")
plt.ylabel("amplituda [V]")
plt.errorbar(np.array(czas), np.array(odl), yerr=np.array(uodl), xerr=np.array(uczas), label='Pomiary prędkości', fmt='bo', capsize=0.5)

plt.show()


def linef(x, a):
    return a * (x - 7.5) / (x + 7.5)


par, cov = curve_fit(linef, czas, odl)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)
u = par


def line(x, a):
    return u * (x - a) / (x + a)


par, cov = curve_fit(line, czas, odl)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)

line = []

for i in czas:
    line.append(u * (i - par[0]) / (i + par[0]))


plt.plot(czas, line, 'r')
plt.show()
plt.savefig('amplituda75.png')
