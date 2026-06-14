#Projectile motion: Euler Method (Without air resistance)
from pylab import *
v=float(input("enter the projectal velocity"))
ang=float(input('Enter  angle of projection '))
vx=v*cos(radians(ang))
vy=v*sin(radians(ang))
g=-9.8
x,y=0,0
t,dt=0,0.01
xpt,ypt=[x],[y]
print( "%-7s\t%-7s\t%-7s" % (' t','x',' y'))
while y >= 0:
    print("%5.2f\t%6.3f\t%6.3f" % (t,x,y))
    x=x+vx*dt
    y=y+vy*dt
    vy=vy+g*dt
    t=t+dt
    xpt.append(x)
    ypt.append(y)
print ('Horizontal Range = %6.3f m' % x)
print ('Time of flight = %6.3f s' % t)
print ('Vertical Height = %6.3f m' % max(ypt))
plot(xpt,ypt)
axhline(0)
xlabel('x')
ylabel('y')
title('Projectile Motion')
show()

