'''from math import*
from numpy import*
wl=float(input("Give the wavelengthof the light"))
h=float(input("Give the distance betwee the slits"))
b=float(input("Give the slit width"))
l=float(input("Give the distance between the scrren and slit"))
y=linspace(-0.015,0.015,1000)
k=float(input("Give the K value"))

beta=.5(k*b*sin(theta))
gama=.5(k*h*sin(theta))
i=i(sin(beta)/beta))**2cos**2(gama)
print(i)
plot(i)'''
import numpy as np
import matplotlib.pyplot as plt

# 1. User Inputs
wl = float(input("Give the wavelength of the light (e.g., 632.8e-9): "))
h = float(input("Give the distance between the slits (e.g., 0.5e-3): "))
b = float(input("Give the slit width (e.g., 0.08e-3): "))
L = float(input("Give the distance between the screen and slit (e.g., 2.0): "))

# 2. Setup Position Array
y = np.linspace(-0.015, 0.015, 1000)

# 3. Wave Vector Calculation
k = (2 * np.pi) / wl

# 4. Geometry transformation
sin_theta = y / L

# 5. Calculate Beta and Gamma
beta = 0.5 * k * b * sin_theta
gama = 0.5 * k * h * sin_theta

# 6. FIXED Intensity Calculation using np.sinc
# This perfectly resolves to 1.0 at the center (y=0)
diffraction_envelope = np.sinc(beta / np.pi)**2
interference_fringes = np.cos(gama)**2

# 7. Define your Maximum Target Intensity (e.g., 1.0 for normalized intensity)
I_max = 1.0 
intensity = I_max * diffraction_envelope * interference_fringes

# 8. Plotting the results
plt.figure(figsize=(10, 5))
plt.plot(y * 1000, intensity, color='blue', label='Interference + Diffraction')
plt.title("Double-Slit Diffraction Envelope & Interference Fringes")
plt.xlabel("Position on screen y (mm)")
plt.ylabel("Intensity I(y)")
plt.grid(True)
plt.show()
