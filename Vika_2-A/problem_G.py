#Prime Number

import math

def check_prime(number):
    if number <= 1:
        return "not prime"
    if number == 2:
        return "prime"
    if number % 2 == 0:
        return "not prime"
    limit = int(math.sqrt(number)) + 1
    for i in range (3, limit, 2):
        if number % i == 0:
            return "not prime"
    return "prime"
    
def main():
    number = int(input())
    print(check_prime(number))

main()