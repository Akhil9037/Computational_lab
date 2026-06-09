from numpy import*
from math import*
from matplotlib.pyplot import*
# newtion rapsion
def f(x):
    return x**4-x-10
def f1(x):
    return 4*x**3
x=float(input("Enter the app Root"))
while(abs(f(x)>0.00000000001)):
    x=x-f(x)/f1(x)
    print(x)
print("The root is",x)
    
