#Another Dimension

import math

diameter_sphere = float(input())

radius = diameter_sphere/2

volume_sphere = ((4/3)*math.pi*(radius**3))
volume_halfsphere = volume_sphere/2

print (volume_halfsphere)