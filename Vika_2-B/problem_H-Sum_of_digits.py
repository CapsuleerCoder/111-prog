#Sum of Digits

number = int(input())
total = 0

for i in range(len(str(number))):             
    remainder = number % 10                   
    total += remainder                        
    number = number // 10                     
    print (number)

print (total)