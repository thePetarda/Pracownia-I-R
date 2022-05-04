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

i = 2
while (i < 16):
    # print(int(sheet.cell_value(i, 2)))
    data.append([int(sheet.cell_value(i, 2)), int(sheet.cell_value(i, 1))])
    udata.append([1, 1])
    i += 1

sorted(data, key=lambda tup: tup[0])

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

plt.xlabel("długośc kabla [m]")
plt.ylabel("czas [ns]")
plt.errorbar(np.array(czas), np.array(odl), yerr=np.array(uodl), xerr=np.array(uczas), label='Pomiary prędkości', fmt='bo', capsize=0.5)

plt.show()


def line(x, a):
    return a * x


par, cov = curve_fit(line, czas, odl)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)

line = []

for i in czas:
    line.append(par[0] * i)


plt.plot(czas, line, 'r')
plt.show()
plt.savefig('predkosc75linia.png')
