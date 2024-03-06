import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt
import numpy as np

data1 = np.loadtxt("data300.txt")
data2 = np.loadtxt("data2.txt")
data3 = np.loadtxt("data3.txt")
data4 = np.loadtxt("data4.txt")
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
#ax.set_title(u'Зависимость от числа Куранта при N=40')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$u$')
ax.plot(data1[:,0], data1[:,1], '-', color = 'red', label=r'$c = 0.9$')
#ax.plot(data2[:,0], data2[:,1], '-', color = 'blue', label=r'$c = 0.6$')
#ax.plot(data3[:,0], data3[:,1], '-', color = 'orange', label=r'$c = 0.9$')
#ax.plot(data4[:,0], data4[:,1], '-', color = 'black', label=r'$c = 1.05$')
ax.legend(loc='best')



plt.show()