#Projectile motion: Euler Method (Without air resistance)
from pylab import *
v=float(input("enter the projectal velocity"))
ang=float(input('Enter velocity ang angle of projection '))
c=float(input("Give the air drag"))
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
    v=sqrt(vx**2+vy**2)
    vx=vx-c*v**2*dt
    
    vy=vy+(g-c*v**2)*dt
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
