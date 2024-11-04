#Sine Wave
import math

N = int(input())
L = int(input())

radians_each_line = (2 * math.pi * N) / L          

for i in range(L):
    x_count = round(20 * (math.sin(i* radians_each_line) + 1))   
    print ("x" * x_count)        