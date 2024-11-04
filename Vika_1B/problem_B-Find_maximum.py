#Find maximum

number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

max_number = number_1

if max_number < number_2:
    max_number = number_2
if max_number < number_3:
    max_number = number_3

print (max_number)