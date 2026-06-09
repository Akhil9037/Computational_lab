from numpy import*
from math import*

n=int(input("no of data points"))
x=[]
y=[]


for i in range(0,n):
    print("enter",i+1,"values")
    x.append(float(eval(input("enter x"))))
    y.append(float(eval(input("enter y"))))

h=x[1]-x[0]
I=y[0]+y[n-1]


for i in range(1,n-1):
    I=I+2*y[i]



I=I*pi*h/2
print("Trap_result",I)


###
from numpy import*
from math import*
n=int(input("no of data points"))
t=[]
v=[]


for i in range(0,n):
    print("enter",i+1,"values")
    t.append(float(eval(input("enter t"))))
    v.append(float(eval(input("enter v"))))

h=t[1]-t[0]
I=v[0]+v[n-1]
for i in range(1,n-1,2):
    I=I+4*v[i]

for i in range(2,n-1,2):
    I=I+2*v[i]



I=I*pi*h/3
print("sim_result",I)

