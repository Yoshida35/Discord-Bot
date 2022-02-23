import math

print("What is the diameter of the circle?")
Diameter = int(input())

Radius = (Diameter/2)

Radiussquared = Radius*Radius

Area = (math.pi * Radiussquared)
Circumference = (math.pi * Diameter)

print("Area =", Area)
print("Circumference =", Circumference)
