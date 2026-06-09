from numpy import*
from math import*
n=60
def f(x):
    return abs(cos(x))**0.5
a= float(input("lower limit"))
b=float(eval(input("upper limit")))
h=(b-a)/60
I= f(a)+f(b)

x=a+2*h
while(x<b):
    I=I+2*f(x)
    x=x+2*h
x=a+h
while(x<b):
    I=I+4*f(x)
    x=x+2*h

sim=I*h/3
print(f"{sim:<15.5f}")
 
############# trap


from numpy import*
from math import*
n=60
def f(x):
    return abs(cos(x))**0.5
a= float(input("lower limit"))
b=float(eval(input("upper limit")))
h=(b-a)/60
I= f(a)+f(b)

x=a+2*h
while(x<b):
    I=I+2*f(x)
    x=x+h
t=I*h/2
print(t)
print(sim-t)


print("="*40)
print(f"{'Method':<20} | {'Result':<15}")
print("-"*40)
print(f"{'Simpson 1/3':<20} | {sim:<15.5f}")
print(f"{'Trapezoidal':<20} | {t:<15.5f}")
print("-"*40)
print(f"Difference (Simp - Trap): {sim - t:.5f}")
print("="*40)
