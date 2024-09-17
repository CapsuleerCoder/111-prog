# Abundant, Deficient, and Perfect Numbers


#Tökum númer og förum í gegnum það með for range loop sem byrjar á einum. ef deiling með tölunni endar með 0 afgang er þetta divisor
# þá bætum við því við summuna, og síðan er bara einföld if skilyrði til þess að kíkja hvaða skilaboð eiga að sendast áfram. 

def sum_of_divisors(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum

def decide(n):
    n = int(n)
    divisor_sum = sum_of_divisors(n)
    if divisor_sum == n:
        return (f"{n} is a perfect number.")
    elif divisor_sum > n:
        return (f"{n} is abundant.")
    else:
        return (f"{n} is deficient.")
    
#print (decide(input()))