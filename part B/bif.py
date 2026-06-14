#Logistic map function
#Bifurcation Diagram
from pylab import *
def f(x):
    return A*x*(1-x)
A=float(input("Enter initial A "))
AF=float(input("Enter final A "))
A0=A
x=.08
xpt=[]
ypt=[]
while(A<=AF):
    for i in range(200):
        x=f(x)
    for i in range(100):
        xpt.append(A)
        ypt.append(f(x))
        x=f(x)
    A=A+.001
plot(xpt,ypt,'.')
title('Logistic map - Bifurcation diagram')
s=str(A0)+'< A < '+str(AF)
xl=(A0+AF)/2.0
print(f"The Bifurcation value:{xl}")
text(xl,.5,s)
xlabel('Control parameter (A)')
ylabel('Population (x)')
show()
