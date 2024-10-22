#Trials and Triangulations

import math

number_a = int(input())
number_b = int(input())
number_c = int(input())
number_s = (number_a+number_b+number_c)/2
triangla_area = math.sqrt(number_s*(number_s-number_a)*(number_s-number_b)*(number_s-number_c))
print (float(triangla_area))