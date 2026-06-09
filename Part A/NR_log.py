from math import*
def f(x):
    return x*log10(x)-4.77
def f1(x):
    return 1+log(x)

x=float(input("Enter The app root"))

while(abs(f(x))>0.000000000000001):

    x=x-f(x)/f1(x)
    print(x)
print("The root is",x)
