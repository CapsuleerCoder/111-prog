#Legendre's Conjecture

import math

def check_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    limit = int(math.sqrt(number)) + 1
    for i in range (3, limit, 2):
        if number % i == 0:
            return False
    return True

def legender_conjucture(number):
    limit = (number+1) ** 2
    number = number ** 2
    print (f"Primes in the range {number} and {limit} are:")
    for i in range(number, limit+1):
        if check_prime(i):
            print (i)

def main():
    number = int(input(""))
    legender_conjucture(number)

main()