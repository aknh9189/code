
# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
get_ipython().magic(u'matplotlib inline')


# In[2]:

water = [0,2,2,3,1.5,1.5,3,2,2,2,2,2.5,2]
alc = [0,2.5,2.5,2.5,2.5,3,2.5,2.5]
weight = [20.9+(0.41*5*x) for x in range(0,13)]
actWater = [(22)+sum(water[:x+1]) for x in range(0,len(water))]
actalc = [(28)+sum(alc[:x+1]) for x in range(0,len(alc))]
print actalc
slopeAlc, intercept = np.polyfit(weight[:len(actalc)], actalc, 1) #mL/g
slopeWater, interssss = np.polyfit(weight, actWater, 1)
print slopeWater,slopeAlc
densityWater = 1/(slopeWater * 0.001)
densityAlc = 1/(slopeAlc * 0.001)
print densityWater, densityAlc


# In[3]:

actualWater = 1000
actualAlc = 789
pErrorWater = (abs(actualWater-densityWater)/actualWater) * 100
pErrorAlc = (abs(actualAlc-densityAlc)/actualAlc) *100
print pErrorWater, pErrorAlc


# In[4]:

plt.figure()
plt.plot(weight,actWater,"o")
plt.plot(weight[:len(actalc)],actalc,"o")
plt.xlabel("Mass (g)")
plt.ylabel("Displacement (mL)")


# In[5]:

x = [0,1,2,3,4]
y = [0,0.5,1,1.5,2]
plt.figure()
plt.plot(y,x)
slope,inter = np.polyfit(y,x,1)
print slope


# In[9]:

densityAlc * (1/100.0**3) *1000


# In[ ]:



