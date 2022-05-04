import numpy as np
import csv
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def positive(data):
    data = np.array(data)
    data = np.delete(data, 2, 1)
    temp = []
    for item in data:
        if (float(item[1]) > 0):
            temp.append([float(item[0]), float(item[1])])
    return temp


def coordinates(data, increment):
    temp_x = np.delete(data, 1, 1)
    temp_y = np.delete(data, 0, 1)
    temp_x = np.array(temp_x).flatten()
    temp_y = np.array(temp_y).flatten()
    temp_t = np.arange(0, increment * (len(temp_x) - 0.1), increment)
    return temp_x, temp_y, temp_t


def scaling(temp_data, min, max):
    max_data = temp_data[0][0]
    min_data = temp_data[len(data) - 1][0]
    constant = (max - min) / (max_data - min_data)
    for number in range(len(data)):
        temp_data[number][0] = (max_data - temp_data[number][0]) * constant + min
    return temp_data


with open('NewFile1.csv', 'r') as f:
    data = list(csv.reader(f, delimiter=","))

inc = float(data[1][3])
data = data[2:]
data = positive(data)
data = scaling(data, 150.01, 735.06)
size = len(data)
print(size)
data1 = data[:int(size / 3)]
data2 = data[int(size / 3):int(2 * size / 3)]
data3 = data[int(2 * size / 3):size]

x1, y1, t1 = coordinates(data1, inc)
x2, y2, t2 = coordinates(data2, inc)
x3, y3, t3 = coordinates(data3, inc)


def fun(x, a, b):
    return a * x + b


popt1, pcov1 = curve_fit(fun, t1, x1)
popt2, pcov2 = curve_fit(fun, t2, x2)
popt3, pcov3 = curve_fit(fun, t3, x3)


def fun1(x):
    return popt1[0] * x + popt1[1]


def fun2(x):
    return popt2[0] * x + popt2[1]


def fun3(x):
    return popt3[0] * x + popt3[1]


optimized_x1 = fun1(t1)
optimized_x2 = fun2(t2)
optimized_x3 = fun3(t3)
print(optimized_x1)

plt.plot(optimized_x1, y1)
plt.plot(optimized_x2, y2)
plt.plot(optimized_x3, y3)
plt.show()

length_laser = 632.8e-9
print(length_laser)
length_vacuum = 0.052
arr_n = []
arr_n_err = []
for number in range(1, 41):
    arr_n.append(1 + length_laser * number / (2 * length_vacuum))
    arr_n_err.append((number*length_laser*0.002)/(2*length_vacuum*length_vacuum))
    print("nr prazka:" + str(number) + " n: " + str(arr_n[number - 1]))

first = [160.49095696, 176.34328159, 191.20483592, 205.07561996, 219.9371743, 237.7710395 , 254.61413441, 269.47568874,
         289.29109452, 305.14341914, 322.97728434, 338.82960897]  # 12
second = [358.53565151, 374.03200384, 394.37096626, 410.8358406, 429.23775899, 445.40224377, 464.10455172,
          482.5064701, 498.97134444, 516.40474081, 533.83813717] #11
third = [553.66022474, 569.64135574, 585.62248675, 600.76250559, 618.42586091, 635.24810407, 654.59368371,
         673.09815118, 693.28484298, 696.72166869, 705.90152535] #11
plt.plot(first,arr_n[:12])
plt.plot(second,arr_n[12:23])
plt.plot(third,arr_n[23:34])
plt.errorbar(first,arr_n[:12],yerr=np.array(arr_n_err[:12]),xerr=2)
plt.errorbar(second,arr_n[12:23],yerr=np.array(arr_n_err[12:23]),xerr=2)
plt.errorbar(third,arr_n[23:34],yerr=np.array(arr_n_err[23:34]),xerr=2)

poptans11, pcovans11 = curve_fit(fun,first,arr_n[:12])
poptans12, pcovans12 = curve_fit(fun,second,arr_n[12:23])
poptans13, pcovans13 = curve_fit(fun,third,arr_n[23:34])
poptans1all, pcovans1all = curve_fit(fun,first+second+third,arr_n[:34])

def funans1(x):
    return poptans11[0]*x+poptans11[1]

def funans2(x):
    return poptans12[0]*x+poptans12[1]

def funans3(x):
    return poptans13[0]*x+poptans13[1]

def funansall(x):
    return poptans1all[0]*x+poptans1all[1]

plt.plot(first,funans1(np.array(first)))
plt.plot(second,funans2(np.array(second)))
plt.plot(third,funans3(np.array(third)))
plt.plot(first+second+third,funansall(np.array(first+second+third)))

print(poptans11,np.sqrt(pcovans11[0][0]),np.sqrt(pcovans11[1][1]), funans1(756.6),756.6*np.sqrt(pcovans11[0][0]))
print(poptans12,np.sqrt(pcovans12[0][0]),np.sqrt(pcovans12[1][1]), funans2(756.6),756.6*np.sqrt(pcovans12[0][0]))
print(poptans13,np.sqrt(pcovans13[0][0]),np.sqrt(pcovans13[1][1]), funans3(756.6),756.6*np.sqrt(pcovans13[0][0]))
print(poptans1all,np.sqrt(pcovans1all[0][0]),np.sqrt(pcovans1all[1][1]), funansall(756.6),756.6*np.sqrt(pcovans1all[0][0]))


plt.show()
