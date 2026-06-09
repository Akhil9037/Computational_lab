import random 

#m=int(input("enter the no iteration"))
m=100
while(m<=10000000):
    n=0
    for i in range(m):
        x=random.random()
        y=random.random()
        r=x**2+y**2
        if r<=1:
            n=n+1
    p=4*float(n)/float(m)
    print(f"{m:<15} {p:<15}")
    m=m*10
    
print("The value of pi=", p)
    
        
