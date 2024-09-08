#Sequence


number_1 = 0
number_2 = 1
number_3 = 0

variable = int(input())

number  = 0

for i in range(variable):
    number = number_1+number_2+number_3
    print (number)
    number_1 = number_2
    number_2 = number_3
    number_3 = number