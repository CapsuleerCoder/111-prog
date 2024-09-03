#Fancy Multiplication

# Í þessu dæmi ætlum við að þykjast eins og * operatorinn er ekki til, og ætlum að nota plús og for loopu til að margfalda. 
# Við byrjum á að taka við 2 int inputum frá notanda, gerum einning total breytu sem við segjum að sé int 0 
# svo gerum við for loop og notum range sem tekur við einum af tölunum, segjum number_1
# í hverri lykkju þá plúsum við hina töluna, segjum number_2 við total breytuna
# að lokum prentum við total


number_1 = int(input()) 
number_2 = int(input())

total = int(0)


for i in range(number_1):    # notum number_1, gætum notað bæði number, þyrfti bara að skipta á báðum stöðum
    total += number_2     # plúsum number_2 við total í hverri lykkjuferð

print (total)  # eftir að lykkjan klárast þá prentum við totalið


#virkar í kattis


