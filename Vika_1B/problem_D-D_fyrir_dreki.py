#D Fyrir Dreki

a = float(input())
b = float(input())
c = float(input())

math_result = (b**2-(4*a*c))

if math_result > 0:
    print (2)
elif math_result == 0:
    print (1)
elif math_result < 0:
    print (0)
