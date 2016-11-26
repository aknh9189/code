
# coding: utf-8

# In[1]:

from matplotlib import pyplot as plt
import numpy as np
import sys
c = 2.99792e8 #define constants 
e = 1.602e-19 # C
h = 6.626e-34 #J s
get_ipython().magic(u'matplotlib inline')


# In[2]:

lamd_5770A = [-0.825, -0.875, -0.888, -0.899] #measured cuttoff voltages for 5770 angstrum filter
lamd_5461A = [-0.950, -0.940, -0.980, -0.913] #all are in volts
lamd_4047A = [-1.821, -1.855, -1.726, -1.878]
lamd_4358A = [-1.430, -1.530, -1.638, -1.676]
ave_voltages = [np.average(lamd_4047A), np.average(lamd_4358A), np.average(lamd_5461A), np.average(lamd_5770A)]
freqs = [c/4047e-10, c/4358e-10, c/5461e-10, c/5770e-10]
kmaxs = list(np.multiply(ave_voltages, -e))


# In[16]:

line, cov = np.polyfit(freqs, kmaxs, 1, cov=True)
h_measured, wkfcn = line
line_stuff = np.linspace(0,10e14,1000)
more_line = np.poly1d(line)


# In[17]:

plt.figure()
plt.plot(freqs, kmaxs,'o', label="Collected Data")
plt.plot(line_stuff, more_line(line_stuff), '--', label="Best Fit")
plt.legend(bbox_to_anchor=(0., 1.1, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Kmax (J)')
plt.show()
#force pyplot to put x axis at zero?


# In[18]:

per_err = abs(h_measured - h)/h*100.0
wkfcn_ev = 6.242e+18 * wkfcn


# In[19]:

per_err


# In[20]:

wkfcn_ev


# In[21]:

h_measured


# In[22]:

weights = [1.0, 1.0, 1.0, 1.0, sys.float_info.epsilon]
x_extra = freqs + freqs[-1:]
y_extra = kmaxs + kmaxs[-1:]
fit_extra, cov_extra = np.polyfit(x_extra, y_extra, 1, w=weights, cov=True)


# In[47]:

fdsa = np.sqrt(np.diag(cov_extra)) * 3


# In[24]:

print kmaxs


# In[37]:

x = np.average(freqs)
x2 = np.average(np.array(freqs)**2)
y = np.average(kmaxs)
xy = np.average(np.array(freqs)*np.array(kmaxs))
n=4.0
dyi= e*0.001#uncertanty in kmaxs is sqrt((q*dkmax/dvstop)^2)
dxi = 10e-9 #ten nm


# In[40]:

xsum = ysum = 0
for a in range(4):
    dmdx = 1/n * (((x2-x**2)*(kmaxs[a]-y))-((xy-x*y)*(2*freqs[a]-2*x)))/((x2-x**2)**2)
    dmdy = 1/n * (freqs[a]-x)/(x2-x**2)
    xsum = xsum + (dmdx * dxi)**2
    ysum = ysum + (dmdy * dyi)**2


# In[41]:

dm = np.sqrt(xsum + ysum)


# In[43]:

print dm #slope


# In[45]:

xsum2 = ysum2 = 0
for a in range(4):
    dmdx = 1/n * (((x2-x**2)*(kmaxs[a]-y))-((xy-x*y)*(2*freqs[a]-2*x)))/((x2-x**2)**2)
    dmdy = 1/n * (freqs[a]-x)/(x2-x**2)
    dbdx = dmdx * x - h_measured * freqs[a]/n
    dbdy = kmaxs[a]/n - dmdy * x
    xsum2 = xsum2 + (dbdx * dxi)**2
    ysum2 = ysum2 + (dbdy * dyi)**2
db = np.sqrt(xsum2+ysum2)


# In[46]:

print db


# In[56]:

err_h = np.sqrt((fdsa[0]**2+dm**2)/2.0)
err_psi = np.sqrt((fdsa[1]**2+db**2)/2)


# In[57]:

print err_h, err_psi


# In[ ]:



