# coding: utf-8

# In[1]:

import matplotlib.pyplot as plt #import modules
import matplotlib.patches as mpatches
import numpy as np
#get_ipython().magic(u'matplotlib inline') # set to inline for ipython


# In[2]:

water = [0,2,2,3,1.5,1.5,3,2,2,2,2,2.5,2] #arrange data from lab
alc = [0,2.5,2.5,2.5,2.5,3,2.5,2.5]

weight = [20.9+(0.41*5*x) for x in range(0,13)] #generate weight array, based on mass of paper clips, in grams

actWater = [(22)+sum(water[:x+1]) for x in range(0,len(water))] #cumulitive sum of water displacement
actalc = [(28)+sum(alc[:x+1]) for x in range(0,len(alc))] #cumultive sum of alc displacement


slopeAlc, intercept = np.polyfit(weight[:len(actalc)], actalc, 1) #mL/g find avereage slope of alc, have to invert to find densitiy
slopeWater, interssss = np.polyfit(weight, actWater, 1) #repeat for water
print slopeWater,slopeAlc #print values

densityWater = 1/(slopeWater * 0.001) #invert and convert to kg/m^3
densityAlc = 1/(slopeAlc * 0.001)

print densityWater, densityAlc #print them


# In[3]:

actualWater = 1000 # finding percent errors in densities kg/m^3
actualAlc = 789 
pErrorWater = (abs(actualWater-densityWater)/actualWater) * 100 #find percent errors
pErrorAlc = (abs(actualAlc-densityAlc)/actualAlc) *100
print pErrorWater, pErrorAlc #print percent errors


# In[4]:

plt.figure() #create figure
plt.plot(weight,actWater,"o") # plot scatter of water vs weight (ml/g)
plt.plot(weight[:len(actalc)],actalc,"o") #plot scatter of actcalc
plt.xlabel("Mass (g)") #add labels
plt.ylabel("Displacement (mL)") #add labels
plt.show() #show figure

# In[5]:

x = [0,1,2,3,4] ##TESTING np.polyfit
y = [0,0.5,1,1.5,2]
plt.figure()
plt.plot(y,x)
slope,inter = np.polyfit(y,x,1)
print slope


# In[9]:

densityAlc * (1/100.0**3) *1000 ##TESTING CONVERSION OF DENSITY


# In[ ]:



