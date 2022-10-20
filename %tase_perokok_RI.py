import csv
import matplotlib.pyplot as plt 
import numpy as np 
from mpl_toolkits.mplot3d import axes3d

perokok= []
with open('Persentase Perokok RI.csv', 'r') as data:
    reader = csv.DictReader(data)
    for i in reader:
        perokok.append(dict(i))
prov = []
t_15 = []
t_16= []
for i in perokok:
    prov.append('{}'.format(i['Provinsi']))
    t_15.append(float(i['2015']))
    t_16.append(float(i['2016']))



x = []
for i1 in range(len(prov)):
    x.append(i1)
y1 = np.repeat(1, len(t_15))
y2 = np.repeat(3, len(t_15))

x1 = []
for i1 in range(0, len(prov)):
    x1.append(i1)

z  = np.zeros(len(prov))
dx = np.zeros(len(prov))
dy = np.ones(len(prov))
tick1 = np.arange(len(prov))



plt.figure("Presentase Perokok Indonesia per Provinsi")
plt.style.use('seaborn-ticks')

ax = plt.subplot(111,projection='3d')
ax.bar3d(x, y1, z, dx, dy, t_15, color='lightblue')
ax.bar3d(x1, y2, z, dx, dy, t_16, color='lightyellow')

plt.xticks(tick1, prov)
plt.yticks([1.5,3.5],[2015,2016])
plt.xticks(rotation=90)
plt.show()