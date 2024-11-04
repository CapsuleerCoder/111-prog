#Pip

n = int(input())

afgangur = 0

while n != 0:
    afgangur = n % 10
    n = n // 10
    if afgangur == 7:
        break

if afgangur == 7:
    print ("the number contains 7.")
else:
    print ("The number does not contain 7. ")