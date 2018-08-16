import numpy as np
import matplotlib.pyplot as plt

# x axis
h = 0.1
x = [i for i in np.arange(0.,10.,h)]

# y axis
y = [np.sin(i) for i in x]


#Plot-----------------------------------------------------
fig = plt.figure(figsize=(20,16), dpi=50)
ax = fig.add_subplot(111)

ax.plot(x,y,linewidth=1,linestyle='-',marker='o',markersize=10,color='k')
ax.set_xlim(0,5)
ax.set_ylim(-1.2,1.2)
ax.set_xlabel('x',fontsize=25)
ax.set_ylabel('sin(x)',fontsize=25)
ax.tick_params(direction='out', length=6, width=2, labelsize=20)

plt.savefig("sine.pdf")
plt.draw()

#plt.show()
