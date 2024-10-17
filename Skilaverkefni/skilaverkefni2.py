#Move
NUMBER_1 = 1
NUMBER_10 = 10
RIGHT = "r"
LEFT = "l"
move = "r"


def initial_pos():
    #Fall sem biður um byrjunarstöðu þangað til það kemur staða sem er gild
    ask_pos = -1
    while not 0 < ask_pos <11: 
        ask_pos = int(input("Position in [1..10]: "))
    return ask_pos

def play_game(char_pos):
    #Meginspilunarfallið, skrifar upp spilaborðið með for loop
    #Spyr hvert á að fara næst innan takmarka sem sett var fyrir
    while (move == RIGHT) or (move == LEFT):
        for x in range(NUMBER_1,NUMBER_10+1):
            if x == char_pos:
                print ("o" ,end="")
            else:
                print ("x", end="")
        print ("\nl: left\nr: right")
        move = input("Move: ")
        if move == RIGHT and char_pos < NUMBER_10:
            char_pos += 1
        elif move == LEFT and char_pos > NUMBER_1:
            char_pos -= 1
        
def main():
    #þetta er bara aðal forrit, ekki alvöru þörf á þessu, bara vani. 
    char_pos = initial_pos()
    play_game(char_pos)

main()