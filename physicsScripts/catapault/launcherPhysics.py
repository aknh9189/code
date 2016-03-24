
# coding: utf-8

# In[ ]:

### Import ###
from matplotlib import pyplot as plt
import numpy as np
get_ipython().magic(u'matplotlib inline')


# In[ ]:

### Basic Constants ###
g=9.81 #m/s*2

### Special Lengths ###
boxLengths = [0.44, 0.29, 0.24] #Length Width Height in meters
marshmellowMasses = [0.008,0.007,0.008,0.007,0.006,0.006,0.008,0.005,0.006,0.005,0.007,0.006,0.006,0.006,0.007,0.007,0.006,0.008,0.006,0.007]
aveMarshMass = np.average(marshmellowMasses) #average mass in kg
 
### Spring Stuff ###
weightOnSpring = 2.412 #kg
stretch = 0.263-0.132 #distance stretches with weight in meters (dx-di)
springk = (weightOnSpring * g)/stretch #find spring constant in N/m

heavySpringConstant = 25/2.2*g/3/(0.112-0.105) #spring constant for the large springs (/3 because 3 holding up weight)
print heavySpringConstant


# In[ ]:

print heavySpringConstant/springk


# In[ ]:

##Finding spring power
distance = 0.05 #meters pulled back
#springs og length =0.162m #spring 1 puleld = 0.189 spring 2 = 0.184
initalPull = ((0.189+0.184)/2.0)-0.162 #meters pulled back in rest position
distance = distance + initalPull #update pullback for forces of springs with initalpullback
plungMass = 0.115 +aveMarshMass#kg accelerated by springs
accuracyTime = 0.0001 #number of seconds per step. 
speed = 0.0 #m/s inital speed
time = 0
forces, accels, speeds, dTraveleds, distances= [],[],[],[],[] #empty for graphing
while (distance-initalPull) >= 0: #while still room for spring to move
    force = 2*springk*(distance) #f=kx two springs
    accel = force/plungMass#f/m = a
    dTraveled = speed*accuracyTime + (accel*(accuracyTime**2.0))/2.0
    speed = speed + accel*accuracyTime #account for acceleration
    distance = distance-dTraveled # update traveled distance
    forces.append(force) #append values
    accels.append(accel)
    speeds.append(speed)
    dTraveleds.append(dTraveled)
    distances.append(distance)
    time = time + accuracyTime #update timing 
    #print "Debug: {0} N | {1} M/s**2 | {2} sec | {3} m/s | {4} m |".format(force, accel, time, speed, distance-initalPull)
    #d = vit + at**2/2
times = np.arange(0,len(forces)*accuracyTime,accuracyTime)

angle = np.deg2rad(45) #angle of inclination
velocity = speed #pull speed from spring calcs
vx,vy = velocity*np.cos(angle), velocity*np.sin(angle) #find inital x and y velocities
if angle == np.deg2rad(45):
    launchHeigh = 0.42 #meters above ground (account for tilt of device) - 0.42@45deg 0.49@60deg
elif angle == np.deg2rad(60):
    launchHeigh = 0.49
landHeight = boxLengths[2] #landing height in meters, from the height of the box
delHeight = launchHeigh - landHeight #find delta h for time calculations
t1 = vy/g #find time until AP
gainedHeight = (vy**2)/(2.0*g) #height gained while prograde
t2 = np.sqrt((2.0 * (delHeight + gainedHeight))/g)
time = t1 + t2
dx = time*vx #find x travel distance
print time
print dx


# In[ ]:

##Plotting Data
plt.figure(figsize=(16, 16))

plt.subplot(221)
plt.plot(times,forces, 'o')
plt.ylabel("Force (N)")
plt.xlabel("Time (s)")
plt.title("Figure 1.4-1: Force vs Time During Launch")

plt.subplot(222)
plt.plot(times,accels, 'o')
plt.ylabel("Acceleration (m/s^2)")
plt.xlabel("Time (s)")
plt.title("Figure 1.4-2: Acceleration vs Time During Launch")

plt.subplot(223)
plt.plot(times,speeds, 'o')
plt.ylabel("Speed (m/s)")
plt.xlabel("Time (s)")
plt.title("Figure 1.4-3: Speed vs Time During Launch")

plt.subplot(224)
plt.plot(distances,forces, 'o')
plt.ylabel("Force (N)")
plt.xlabel("Distance from Equilibrium (m)")
plt.title("Figure 1.4-4: Force Distance Ratio During Launch")

plt.show()


# In[ ]:

#plot energy triangle
plt.figure()
plt.plot(forces, distances, 'o')
plt.title("Figure 1.1: Force vs Distance Graph of spring")
plt.xlabel("Force (N)")
plt.ylabel("Distance from Equilibrium (m)")


# In[ ]:

##IGNORE (Repeat of finding distance)
angle = np.deg2rad(45) #angle of inclination
velocity = speed #pull speed from spring calcs
vx,vy = velocity*np.cos(angle), velocity*np.sin(angle) #find inital x and y velocities
if angle == np.deg2rad(45):
    launchHeigh = 0.42 #meters above ground (account for tilt of device) - 0.42@45deg 0.49@60deg
elif angle == np.deg2rad(60):
    launchHeigh = 0.49
landHeight = 0#boxLengths[2] #landing height in meters, from the height of the box
delHeight = launchHeigh - landHeight #find delta h for time calculations
t1 = vy/g #find time until AP
gainedHeight = (vy**2)/(2.0*g) #height gained while prograde
t2 = np.sqrt((2.0 * (delHeight + gainedHeight))/g)
time = t1 + t2
dx = time*vx #find x travel distance
print dx


# In[ ]:

#plotting predicted paths
angle = np.deg2rad(45) #angle of inclination
velocity = speed #pull speed from spring calcs
vx,vy = velocity*np.cos(angle), velocity*np.sin(angle) #find inital x and y velocities
if angle == np.deg2rad(45):
    launchHeigh = 0.42 #meters above ground (account for tilt of device) - 0.42@45deg 0.49@60deg
elif angle == np.deg2rad(60):
    launchHeigh = 0.49
h = launchHeigh
x = 0
timeRes = 0.01
xs, hs = [],[]
while h >= 0:
    x = x + vx*timeRes
    vy = vy + (timeRes*-9.81)
    h = h + vy*timeRes
    xs.append(x)
    hs.append(h)
plt.figure()
plt.plot(xs,hs,'o')
plt.xlabel("Meters")
plt.ylabel("Meters")
plt.show()


# In[ ]:

#finding percent error
measured=0.9919
act = 0.9998
error = abs(measured-act)/act*100.0
print error


# In[ ]:




# In[ ]:




# In[ ]:



