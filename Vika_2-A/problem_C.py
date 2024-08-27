#The Warm Summer

answer = input("You need something doubled? (Y)es? ")



while answer == "Y":
    number = float(input("All right, then. Give me a number, and I'll double it for ya: "))
    double_number = number * 2
    print ("%f" % double_number)
    answer = input("You need something else doubled? (Y)es? ")

