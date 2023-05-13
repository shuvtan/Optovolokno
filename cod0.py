'''Обратная задача - определяем 1)количество катушек, 
                                2)координаты начала и конца мёртвых зон, 
                                3)конец линии'''

import math as m
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import warnings
warnings.filterwarnings("ignore")


#Считываем данные файла
with open('C:/Users/User/Desktop/Optovolokno/MERTV1310-2000.txt') as f:
        data = [float(x) for x in (' ').join(f.readlines()).split()]
        data = np.array(data)
km = np.linspace(0,25000,len(data))

s = len(data)

#Построение рефлектограммы
fig, ax = plt.subplots(figsize=(8, 7), dpi=150)
plt.title("Рефлектограмма",color="black", fontweight="bold") # заголовок
plt.xlabel("")
plt.ylabel("")
#plt.xlim([16000, 18000])

plt.minorticks_on()
plt.grid(which='major',
        color = 'grey', 
        linewidth = 0.7)
plt.grid(which='minor', 
        color = 'grey', 
        linestyle = ':')

ax.plot(km, data, "darkorange", linewidth = 0.5)
#ax.legend()

d1 = [0]
for i in range(1,s-1):
    d1.append(abs(data[i+1]-data[i]))
d1.append(0)

d1 = np.array(d1)
d11 = d1[:-50]
d111=[]
for i in range(50):
    if d11[i]!=0:
        d111.append(d11[i])
        
mean_d1 = np.mean(np.array(d111))

#Построение графика дельт
'''fig, ax = plt.subplots(figsize=(8, 7), dpi=150)
plt.title("Значения дельт",color="black", fontweight="bold") # заголовок
plt.xlabel("") # ось абсцисс
plt.ylabel("") # ось ординат
plt.xlim([0, 40])

plt.minorticks_on()
plt.grid(which='major',
        color = 'grey', 
        linewidth = 0.7)
plt.grid(which='minor', 
        color = 'grey', 
        linestyle = ':')
ax.plot(km, d1, color = "darkorange", linewidth = 1)
#ax.legend()
#print(mean_d1)'''

ends1=[]
k=[]
for i in range(1,s-1):
    if d1[i]-d1[i-1]>=mean_d1 and d1[i]-d1[i+1]>=mean_d1:
        ends1.append(i+1)
#print(ends1)


mertv2 = []
mertv1 = [ends1[0]]
for i in range(0, len(ends1)-1):
    if ends1[i+1]-ends1[i]>=100:
        mertv2.append(ends1[i])
        mertv1.append(ends1[i+1])
    if (sum(ends1, start=i)/len(ends1)-i) - ends1[i]<10:
        break

print(mertv1, mertv2)

def mapping(x, a, b): 
    return a*x+b

#Определение конца линии
#/////////////////////
for i in range(-2, -len(mertv1), -1):
    popt, pcov = optimize.curve_fit(mapping, km[mertv1[i]+50:mertv1[i]+500], data[mertv1[i]+50:mertv1[i]+500])
    a, b = popt
    err = np.sqrt(np.diag(pcov))
    if err[1]>10:
        mertv1 = mertv1[0:i+1]
        mertv2 = mertv2[0:i+1]
        break
          
print("Количество катушек:", len(mertv1)-1)
print("Координата конца линии:", mertv1[-1], "[м]")
#///////////////////

for i in range(0,len(mertv2)):
    print("Координата начала", i+1, "катушки:", mertv2[i], "[м]")