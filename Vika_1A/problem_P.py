#Painting the roof

import math

length = 50

degree = int(input())

radians = math.radians(degree)

height = length * math.tan(radians)

print (round(height,1))