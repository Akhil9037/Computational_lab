





#######################






























# Useful imports

from matplotlib.pyplot import*
from scipy import constants
import numpy as np
import matplotlib.pyplot as plt

# Define relevant parameters

q1 = constants.e * 79  # Large nucleus charge
q2 = constants.e * 2   # Small nuclear charge
m = 6.64424e-27       # Small nucleus mass
v0 = 1e7              # Initial velocity

# Define a Coulomb potential
def Coulomb(r,Q,q):
    return Q*q/(4*np.pi*constants.epsilon_0*np.linalg.norm(r)**3) * r


r_int = q1*q2/(2*np.pi*constants.epsilon_0*m*v0**2)
print(r_int)
sd = 1e-12            # Size of simulation domain (in z axis)
dt = 1e-22            # Simulation time step

# Define a function to simulate ion trajectory
def collide(b):
    rvals = []  # A list to record the trajectory of the particle for plotting
    r = np.array([b,0.0,-sd])   # Initial particle position
    v = np.array([0.0,0.0,v0])  # Initial particle velocity
    
    exited = False
    while not exited:
        rvals.append(r.copy())  # Record current position
        
        # Evaluate Coulomb force and take an Euler step
        v += dt * Coulomb(r,q1,q2) / m  
        r += dt * v
        
        # If the particle z-position is outside of the simulation domain, terminate
        if np.abs(r[2]) > sd:
            exited = True
            
    # return the particle trajectory
    return rvals



# Figure set up
fig,ax = plt.subplots(figsize=(6,6))
ax.set_xlim((-1e-12,1e-12))
ax.set_ylim((-1e-12,1e-12))
ax.plot([0.0],[0.0],'ro')
ax.set_aspect(aspect=1.0)

for b in np.linspace(-3e-13,4.0e-13,9):
    rv = collide(b)
    rv = np.array(rv)
    ax.plot(rv[:,0],rv[:,2],'b')
