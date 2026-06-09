from numpy import*
tf=float(input("Enter the final time"))
h=float(input("Enter the time step size"))
n=round(tf/h)
time=zeros(n+1,dtype=float)
nucl=zeros(n+1,dtype=float)
lam=float(input("Enter the disintegration constant"))
nucl[0]=int(input("Enter the initial number of nuclei"))
time[0]=0.0
print(f"{'Time':<15} {'The remaining nucles':<15}")
for i in range(0,n):
    nucl[i+1]=nucl[i]*(1-h*lam)
    time[i+1]=time[i]+h
print(f"{time[i+1]:<15.5f} {nucl[i+1]:<15.5f}")
# Calculate and print N(t_1/2)
half_life_nuclei = nucl[0] / 2
print("-" * 35)
print(f"N(t_1/2) target value: {half_life_nuclei}")
