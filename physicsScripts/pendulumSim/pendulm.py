
# coding: utf-8

# In[ ]:

## 30 40 50 #mass = 500g length = 0.69m ##IMPORT/DATA
angleTrials = [7.45, 8.12, 8.29]
## 100g 300g 500g#lengh = 0.69 angle = 40
massTrials = [8.085, 8.105, 8.188]
## 0.29 0.49 0.69 #mass = 500g #angle = 40
lengthTrials = []
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
#%matplotlib inline


# In[ ]:




# In[ ]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
f1, f2 = plt.subplots()
x= np.arange(0,2*np.pi,0.01)
line = f2.plot(x, x*5)
def animate(i):
    line.set_ydata(np.sin(x + i/10.0))  # update the data
    return line,


# In[ ]:




# In[ ]:

animation.FuncAnimation? #FOR ANIMATION


# In[ ]:

##PENDULUM SIMULATION
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random
import time
from matplotlib import style
#%matplotlib inline
#style.use('fivethirtyeight')
fig = plt.figure()

ax1 = fig.add_subplot(1,1,1)
ax1.xlabel ='meters'
ax1.ylabel = 'meters'

#5
g=9.8
length = 2.5 #3m
mass = 666 #kg
angle = 400 #degrees from center 
def findAngle(time):
    return angle*np.sin(np.deg2rad((np.sqrt((g/length) )))* (time*10.0))#find angle based on time, using equation from hperphysics
def animate(i):
    xs=[0,(length*np.sin(np.deg2rad(findAngle(i))))]#find x and y points using findtime
    ys=[0,-(length*np.cos(np.deg2rad(findAngle(i))))]
    ax1.clear()
    ax1.set_ylim([-5,5])
    ax1.set_xlim([-5,5])
    ax1.plot(xs,ys)
    plt.text(0,0.5,(i/5.0*1.7),fontsize='12')
ani = animation.FuncAnimation(fig, animate, np.arange(0,1000), interval=100, blit=False)#animate functions
plt.show()

##TODO
#GET ANGLE TO START AT DESIRED STARTING POINT
#FIX ERRORS IN 
#BUMP UP FRAMERATE
##ENDTODO


# 

# In[ ]:

get_ipython().magic(u'matplotlib inline ##TESTING FOR ANGLE OVER TIME (SIN)')
fig1=plt.figure()
plt.plot(range(0,19.5,0.5), [findAngle(x) for x in range(0,19.5,0.5)])
fig1.show()


# In[ ]:




# In[31]:

from matplotlib import pyplot as plt #FIND AVREAGE SLOPE AND PERIODS FOR GRAPH
import numpy as np
get_ipython().magic(u'matplotlib inline')
lengths = [0.29,0.49,0.69]
ts = [1.02,1.38,1.62]
#t = [(2*np.pi)*x/9.8 for x in lengths]
t2 = [x**2 for x in ts]

slope, inter = np.polyfit(lengths,t2, 1)
print 1/((slope)*(1/(4*np.pi**2)))
print slope


# In[25]:

fig = plt.figure() #GRAPH DATA
plt.plot(lengths, t2, 'o')
plt.plot([0.2,0.7], [slope*x for x in [0.2,0.7]], '--')
plt.xlabel("Length (meters)")
plt.ylabel("Period^2 (seconds)")
plt.show()


# In[ ]:

import numpy as np
angle30s = [12.4, 23.5, 25, 25]
np.average(angle30s)


# In[ ]:

plt.plot(lenght, [x**2 for x in timeL])

