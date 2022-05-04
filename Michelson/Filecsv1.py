import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def press(el, min, max):
    max_el = 4.32
    # max_el = data[len(data) - 1][0]
    min_el = 0.52
    # min_el = data[0][0]
    const = (max - min)/(max_el - min_el)
    return (max_el - el)*const + min


data = []
with open('NewFile1.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    i = 0
    for row in csv_reader:
        if i > 1:
            # print(float(row[0]))
            data.append((press(float(row[0]), 0.05, 101.12), float(row[1])))
        i += 1

# print(sorted(data, key=lambda tup: tup[0]))
# sorted(data, key=lambda tup: tup[0], reverse=True)
data.sort(key=lambda tup: tup[0], reverse=True)


cisnienie = []
dioda = []

for el in data:
    cisnienie.append(el[0])
    dioda.append(el[1])

# for el in data:
#     print(el[0])

# print(dioda)

cisn = np.array(cisnienie)
diod = np.array(dioda)

plt.plot(cisn, diod, 'b')
plt.show()
plt.savefig('Szum1.png')
plt.clf()

maksima = []
cmaks = []
liczby = []

i = 2
while(i < len(data) - 2):
    if ((dioda[i] > dioda[i-1]) and (dioda[i] < dioda[i+1]) and (dioda[i] > 1)):
        maksima.append(dioda[i])
        cmaks.append(cisnienie[i])
        liczby.append(len(liczby))
    i += 1

print(data)

wsp = []
i = 1
for el in cmaks:
    lam = 632.8
    d = 5.2
    n = 1 + (i*lam)/(2 * d)
    wsp.append(n)
    i += 1

cmaksm = np.array(cmaks)
n = np.array(wsp)

plt.plot(cmaksm, n, 'b')

plt.show()


def line(x, a, b):
    return a * x + b


par, cov = curve_fit(line, cmaksm, n)

print(par)
perr = np.sqrt(np.diag(cov))
# print(cov)
print(perr)

line = []

for i in cmaksm:
    line.append(par[0] * i + par[1])


plt.plot(cmaksm, line, 'r')
plt.show()
plt.savefig('Wsp1.png')
