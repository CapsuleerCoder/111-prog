#Sum of Powers 

base_number = int(input(""))
length_number = int(input(""))

total = 0

for i in range(0, length_number, 1):        
    exponent = int(input())                 
    total += (base_number**exponent)       

print (total)