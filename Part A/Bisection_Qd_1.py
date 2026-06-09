from math import*
from numpy import*

def f(x):
    return x**3-12

from math import *
a=float(input("Enter the initial root"))  
b=float(input("Enter the Upper root"))   
c=(a+b)/2
print (c)
print(f"{'a':<15} {'b':<15} {'c':<15} {'f(c)':<15}")
print("-"*70)

while (abs(f(c))>0.000000000001):
    print(f"{a:<15.5f} {b:<15.10f} {c:<15.10f} {f(c):<15.10f}")

    if (f(c)>0.0):
        a=a
        b=c
        c=(a+b)/2
        #print (c)
    elif (f(c)<0.0):
       a=c
       b=b
       c=(a+b)/2
       #print (c)
    

print ("Final root is :",c)

   
