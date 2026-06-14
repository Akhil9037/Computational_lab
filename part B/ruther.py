from matplotlib.pyplot import *
from math import *
from numpy import*
import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 21.7895       # Coulomb-like constant
dt = 0.001        # time step
steps = 5000      # number of integration steps

# Arrays for impact parameters and results
b = np.linspace(0, 1, 10)
cotthetaby2 = np.zeros(len(b))

# Function to compute acceleration under central inverse-square law
def acceleration(x, y):
    r2 = x**2 + y**2
    r32 = r2**1.5
    ax = c * x / r32
    ay = c * y / r32
    return ax, ay

# RK4 step for position and velocity
def rk4_step(x, y, vx, vy, dt):
    # k1
    ax1, ay1 = acceleration(x, y)
    k1vx, k1vy = ax1*dt, ay1*dt
    k1x, k1y = vx*dt, vy*dt

    # k2
    ax2, ay2 = acceleration(x + 0.5*k1x, y + 0.5*k1y)
    k2vx, k2vy = ax2*dt, ay2*dt
    k2x, k2y = (vx + 0.5*k1vx)*dt, (vy + 0.5*k1vy)*dt

    # k3
    ax3, ay3 = acceleration(x + 0.5*k2x, y + 0.5*k2y)
    k3vx, k3vy = ax3*dt, ay3*dt
    k3x, k3y = (vx + 0.5*k2vx)*dt, (vy + 0.5*k2vy)*dt

    # k4
    ax4, ay4 = acceleration(x + k3x, y + k3y)
    k4vx, k4vy = ax4*dt, ay4*dt
    k4x, k4y = (vx + k3vx)*dt, (vy + k3vy)*dt

    # Update velocity and position
    vx_new = vx + (k1vx + 2*k2vx + 2*k3vx + k4vx)/6
    vy_new = vy + (k1vy + 2*k2vy + 2*k3vy + k4vy)/6
    x_new  = x  + (k1x  + 2*k2x  + 2*k3x  + k4x )/6
    y_new  = y  + (k1y  + 2*k2y  + 2*k3y  + k4y )/6

    return x_new, y_new, vx_new, vy_new

# Simulation loop
plt.figure(figsize=(10,6))

for j in range(len(b)):
    # Initial conditions
    x, y = -5.0, b[j]
    vx, vy = 10.0, 0.0

    traj_x, traj_y = [x], [y]

    for i in range(steps):
        x, y, vx, vy = rk4_step(x, y, vx, vy, dt)
        traj_x.append(x)
        traj_y.append(y)

    # Store scattering angle using final velocity vector
    theta = np.arctan2(vy, vx)   # final angle
    cotthetaby2[j] = 1/np.tan(theta/2)

    # Plot trajectory
    plt.subplot(2,1,1)
    plt.plot(traj_x, traj_y)

# Plot scattering relation
plt.subplot(2,1,1)
plt.title("Trajectories under Coulomb force")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(2,1,2)
plt.plot(b, cotthetaby2, 'o-')
plt.title("Impact parameter vs cot(theta/2)")
plt.xlabel("Impact parameter b")
plt.ylabel("cot(theta/2)")

plt.tight_layout()
plt.show()
from matplotlib.pyplot import *
from math import *
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

# Constants
c = 21.7895          # k*q1*q2/m (effective Coulomb constant)
dt = 0.001
steps = 20000

# Impact parameters
b = np.linspace(0.05, 1.0, 10)
cotthetaby2 = np.zeros(len(b))


# Coulomb acceleration
def acceleration(x, y):
    r2 = x*x + y*y
    r32 = r2**1.5

    ax = c*x/r32
    ay = c*y/r32

    return ax, ay


# RK4 integrator
def rk4_step(x, y, vx, vy, dt):

    ax1, ay1 = acceleration(x,y)
    k1x = vx*dt
    k1y = vy*dt
    k1vx = ax1*dt
    k1vy = ay1*dt


    ax2, ay2 = acceleration(x+k1x/2,y+k1y/2)
    k2x = (vx+k1vx/2)*dt
    k2y = (vy+k1vy/2)*dt
    k2vx = ax2*dt
    k2vy = ay2*dt


    ax3, ay3 = acceleration(x+k2x/2,y+k2y/2)
    k3x = (vx+k2vx/2)*dt
    k3y = (vy+k2vy/2)*dt
    k3vx = ax3*dt
    k3vy = ay3*dt


    ax4, ay4 = acceleration(x+k3x,y+k3y)
    k4x = (vx+k3vx)*dt
    k4y = (vy+k3vy)*dt
    k4vx = ax4*dt
    k4vy = ay4*dt


    x += (k1x+2*k2x+2*k3x+k4x)/6
    y += (k1y+2*k2y+2*k3y+k4y)/6

    vx += (k1vx+2*k2vx+2*k3vx+k4vx)/6
    vy += (k1vy+2*k2vy+2*k3vy+k4vy)/6


    return x,y,vx,vy



figure(figsize=(8,8))


for j in range(len(b)):

    # initial particle position and velocity
    x = -10
    y = b[j]

    vx = 10
    vy = 0


    traj_x=[x]
    traj_y=[y]


    for i in range(steps):

        x,y,vx,vy = rk4_step(x,y,vx,vy,dt)

        traj_x.append(x)
        traj_y.append(y)


    # scattering angle
    theta = np.arctan2(vy,vx)

    cotthetaby2[j] = 1/tan(theta/2)


    # trajectory plot
    subplot(2,1,1)
    plot(traj_x,traj_y)


subplot(2,1,1)

xlabel("x")
ylabel("y")
title("Rutherford scattering trajectories")
grid()


subplot(2,1,2)

plot(b,cotthetaby2,'o-')

xlabel("Impact parameter b")
ylabel("cot(theta/2)")
title("Rutherford relation")

grid()

tight_layout()
show()


c=21.7895
dt=0.0001
x=zeros(10001,float)
y=zeros(10001,float)
b=linspace(0,1,10)
cotthetaby2=zeros(10,float)
for j in range(1,10):
    x[0],y[0],vy,vx,t=-5,b[j],0,10,0
    for i in range(10000):
        vx=vx+c*x[i]*dt/(x[i]**2+y[i]**2)**1.5
        vy=vy+c*y[i]*dt/(x[i]**2+y[i]**2)**1.5
        x[i+1]=x[i]+vx*dt
        y[i+1]=y[i]+vy*dt
    cotthetaby2[j]=((x[i]-x[0])/(y[i]-y[0]))
    subplot(2,1,1)
    plot(x,y)
title("TJ")
#xlabel("x")ylabel("y")
subplot(2,1,2)
plot(b,cotthetaby2)
#xlable("imp")ylable("ctb2")
show()


c = 5.44
dt = 0.001  # Slightly larger time step to help it travel further
v = float(input('Enter the velocity (e.g., 5): '))

# Increase steps or time so the particle actually escapes the nucleus zone
steps = 20000 
x = zeros(steps + 1, 'float')
y = zeros(steps + 1, 'float')

b = linspace(0.1, 1.0, 10)  
cb2 = zeros(10, 'float')

# Loop through all 10 impact parameters
for j in range(10):
    # Start further back if velocity is high, or adjust steps
    x[0], y[0], vx, vy = -10.0, b[j], v, 0.0
    
    for i in range(steps):
        x[i+1] = x[i] + vx * dt
        y[i+1] = y[i] + vy * dt
        
        r_cubed = (x[i]*x[i] + y[i]*y[i])**1.5
        vx = vx - (x[i] * c * dt) / r_cubed
        vy = vy - (y[i] * c * dt) / r_cubed
        
    # Plot trajectory for this specific impact parameter
    figure(1)
    plot(x, y)
    
    # FIX: Calculate theta IMMEDIATELY while vx and vy belong to this 'j'
    theta = atan2(vy, vx)
    cb2[j] = 1.0 / tan(theta / 2.0)

# Trajectory Plot Adjustments
figure(1)
xlabel('x')
ylabel('y')
title('Rutherford scattering: trajectory of alpha particle')
grid(True)
axis('equal') # Keeps the scale 1:1 so angles look physically correct

# Impact Parameter Plot
figure(2)
plot(b, cb2, 'bo-')
xlabel('Impact parameter (b)')
ylabel('cot(theta/2)')
title('Impact parameter vs cot(theta/2)')
grid(True)

show()


from pylab import *
from math import *

c = 5.44
dt = 0.001
v = float(input('Enter the velocity (e.g., 5): '))

# 1. Expand 'b' to simulate a wider area of empty space around the nucleus
# Most rays will have a large 'b' (passing far away), matching reality.
b = linspace(0.05, 15.0, 500)  

# Counters for our categories
passed_straight = 0
deflected_small = 0
backscattered = 0

steps = 15000
x = zeros(steps + 1, 'float')
y = zeros(steps + 1, 'float')

for j in range(len(b)):
    # Start further back so the high-impact parameters have time to approach
    x[0], y[0], vx, vy = -15.0, b[j], v, 0.0
    
    for i in range(steps):
        x[i+1] = x[i] + vx * dt
        y[i+1] = y[i] + vy * dt
        
        r_cubed = (x[i]*x[i] + y[i]*y[i])**1.5
        vx = vx - (x[i] * c * dt) / r_cubed
        vy = vy - (y[i] * c * dt) / r_cubed
        
    # Calculate final scattering angle in degrees
    theta = abs(deg2rad(atan2(vy, vx)))
    theta_deg = degrees(atan2(vy, vx))
    
    # Classify the ray based on its final deflection angle
    if abs(theta_deg) < 5.0:
        passed_straight += 1
    elif abs(theta_deg) >= 90.0:
        backscattered += 1
    else:
        deflected_small += 1

    # Optional: Plot every 10th trajectory so the graph isn't too crowded
    if j % 10 == 0:
        figure(1)
        plot(x, y, 'b-', alpha=0.5)

# --- Format Trajectory Plot ---
figure(1)
plot(0, 0, 'ro', markersize=8, label='Gold Nucleus') # Mark the central positive nucleus
xlabel('x')
ylabel('y')
title('Rutherford Scattering: Particle Rays')
axis([-15, 15, -2, 15])
grid(True)

# --- Display the Final Stats ---
total_particles = len(b)
print("\n=== SCATTERING EXPERIMENT RESULTS ===")
print(f"Total incoming rays simulated: {total_particles}")
print(f"Passed straight through (< 5°): {passed_straight} ({passed_straight/total_particles*100:.1f}%)")
print(f"Deflected at small angles:      {deflected_small} ({deflected_small/total_particles*100:.1f}%)")
print(f"Backscattered (> 90° to 180°):  {backscattered} ({backscattered/total_particles*100:.1f}%)")

show()
