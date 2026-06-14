# Simple harmonic oscillator (un-damped)
# Euler method
from matplotlib.pylab import *
w=5.0 # Change omega here
t,x,v=0,1.0,0
dt=0.01
m=float(input("Enter mass of the pendulum"))
tmax=10
xl=[x]
vl=[v]
tl=[t]
p1=[m*v]

print(f"{'t':<15}{'x':<15}{'v':<15} {'p':<15}")
while t < tmax:
    x=x+v*dt
    v=v-dt*w*x
    p=m*v
    
    t=t+dt
    print(f"{t:<15.5f},{x:<15.5f},{v:<15.5f},{p:<15.5f}")
    vl.append(v)
    xl.append(x)
    tl.append(t)
    p1.append(p)

subplot(2,2,1)
axhline(0)
xlabel("t")
ylabel("x")
plot(tl,xl)
subplot(2,2,2)
axhline(0)
xlabel("t")
ylabel("v")
plot(tl,vl,"r")
subplot(2,2,3)
axhline(0)
axvline(0)
xlabel("x")
ylabel("v")
plot(xl,vl,"m")

subplot(2,2,4)
axhline(0)
axvline(0)
xlabel("x")
ylabel("p")
plot(xl,p1,"b")
show()
