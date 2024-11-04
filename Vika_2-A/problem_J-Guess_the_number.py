#Guess the Number

lowest = 1
highest = 1000
guess_count = 0 
answer = ""

while (guess_count < 10) and (answer != "correct"):
    guess = ((lowest + highest) // 2)
    print (guess)
    answer = input("")

    if answer == "higher":
        lowest = guess+1
    elif answer == "lower":
        highest = guess-1

    guess_count +=1 