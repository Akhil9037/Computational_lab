def f(x,y):
    return (1/10)*(x**2+y**2)

print ("RK 4 method")
x=0.0
y=1.0
h=0.1
print ("x","y")
print (f"{'x':<15},{'y':<15}")
print (x,y)

while (x<0.4):
    k1=h*f(x,y)
    k2=h*f(x+h/2,y+k1/2)
    k3=h*f(x+h/2,y+k2/2)
    k4=h*f(x+h,y+k3)
    y=y+(k1+2*k2+2*k3+k4)/6
    x=x+h
    print (f"{x:<15.5f},{y:<15.5f}")

print(f"Final Value of x: {x:.5f}")
print(f"Final Value of y: {y:.5f}")
