#Collatz Conjecture

a = int(input())
print (a)

while a != 1:
    if a % 2 == 0:
        a = int(a/2)
    elif a % 2 != 0:
        a = int((a*3)+1)
    print (a)





5
