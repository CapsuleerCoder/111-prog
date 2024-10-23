#Euclid's GCD

def euclid(number_a, number_b):
    while number_b != 0:
        temp = number_b
        number_b = number_a % number_b
        number_a = temp
    return number_a

def main():
    number_a = int(input(""))
    number_b = int(input(""))
    print (euclid(number_a, number_b))

main()