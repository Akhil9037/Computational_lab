from numpy import*
from math import*

n=int(input("no of data points"))
xl=[]
yl=[]


for i in range(0,n):
    print("enter",i+1,"values")
    xl.append(float(eval(input("enter x"))))
    yl.append(float(eval(input("enter y"))))
s=0
x=float(eval(input("enter the interpolation value")))
for i in range(n):
    p=1
    for j in range(n):
        if i!=j:
            p=p*(x-xl[j])/(xl[i]-xl[j])
    s=s+p*yl[i]
print("the inter polation value",s)
