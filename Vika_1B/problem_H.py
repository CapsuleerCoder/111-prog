#Rock, Paper, Scissors

player_1 = input()
player_2 = input()

if player_1 == player_2:
    print ("Draw")
elif (player_1 == "rock" and player_2 == "scissors") or (player_1 == "scissors" and player_2 == "paper") or (player_1 == "paper" and player_2 == "rock"):
    print ("Player 1")
else:
    print ("player 2")