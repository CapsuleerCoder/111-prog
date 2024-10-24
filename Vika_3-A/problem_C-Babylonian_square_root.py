# Babylonian Square Root Algorithm

def get_inputs():
    n_integer = int(input())
    g_integer = int(input())
    t_float = float(input())
    return n_integer, g_integer, t_float

def babylon(square_root, guess, tolerance):
    count = 1
    new_guess = ((square_root/guess)+guess)/2
    #print (f"Guess: {guess}, new_guess: {new_guess}")
    while abs(guess-new_guess) > tolerance:
        #print (abs(guess-new_guess))
        guess = new_guess
        new_guess = ((square_root/guess)+guess)/2
        count += 1
    return int(count), new_guess

def main():
    square_root, inital_guess, tolerance = get_inputs()
    count, babylon_number = babylon(square_root, inital_guess, tolerance)
    print (f"{babylon_number :.5}")
    print (count)

main()