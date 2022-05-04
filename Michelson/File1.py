# Reading an excel file using Python
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Give the location of the file
loc = ("Pomiary1.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

# For row 0 and column 0
# x = sheet.cell_value(4, 0)
# print(x) 
# x = float(x)
# x += 2
# print(x)

# Extracting number of rows
print(sheet.nrows)


def press(el, min, max):
    max_el = float(sheet.cell_value(1, 0))
    min_el = float(sheet.cell_value(sheet.nrows-3, 0))
    const = (max - min)/(max_el - min_el)
    return (max_el - el)*const + min


cisnienie = []
dioda = []

i = 1
while (i < sheet.nrows - 2):
    cisnienie.append(press(float(sheet.cell_value(i, 0)), 0.05, 101.12))
    dioda.append(float(sheet.cell_value(i, 1)))
    i += 1

cisn = np.array(cisnienie)
diod = np.array(dioda)

print(cisnienie)
plt.plot(cisn, diod, 'b')
plt.show()
plt.savefig('Szum1.png')
plt.clf()

# maksima = []
# cmaks = []
# liczby = []

# i = 2
# while(i < sheet.nrows - 5):
#     if ((dioda[i] > dioda[i-1]) and (dioda[i] > dioda[i-2]) and (dioda[i] < dioda[i+1]) and (dioda[i] < dioda[i+2])):
#         maksima.append(dioda[i])
#         cmaks.append(cisnienie[i])
#         liczby.append(len(liczby))
#     i += 1

# wsp = []
# i = 1
# for el in cmaks:
#     lam = 632.8
#     d = 1
#     n = 1 + (i*lam)/(2 * d)
#     wsp.append(n)
#     i += 1

# cmaksm = np.array(cmaks)
# n = np.array(wsp)

# plt.plot(cmaksm, n, 'b')

# plt.show()


# def line(x, a, b):
#     return a * x + b


# par, cov = curve_fit(line, cmaksm, n)

# print(par)
# perr = np.sqrt(np.diag(cov))
# # print(cov)
# print(perr)

# line = []

# for i in cmaksm:
#     line.append(par[0] + par[1]/i)


# plt.plot(cmaksm, line, 'r')
# plt.show()
# plt.savefig('Wsp1.png')
