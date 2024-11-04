#Maximum Number

def input_numbers():
    list_of_numbers = []
    number = 1
    while number > 0:
        number = int(input())
        list_of_numbers.append(number)
    return list_of_numbers

def find_max(list_of_numbers):
    max_number = 0
    for number in list_of_numbers:
        if number > max_number:
            max_number = number
    return max_number

def main():
    list_of_numbers = input_numbers()
    max_number  = find_max(list_of_numbers)
    print (max_number)

main()