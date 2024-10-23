#Leap Year

y = int(input())

flag = False

if y % 400 == 0:
    flag = True
elif y % 100 == 0:
    flag = False
elif y % 4 == 0:
    flag = True

if flag:
    print ("True")
else:
    print ("False")
