#The Leftovers

number_players = 0
sum_of_hands = 0

while number_players < 2:
    number_players = int(input())

for x in range(number_players):
    current_play = int(input())
    sum_of_hands += current_play

decide_winner = sum_of_hands % number_players

print (f"The sum of all contributions is {sum_of_hands}")
print (f"When {sum_of_hands} is divided by {number_players}, the remainder is {decide_winner}")
print (f"Player {decide_winner} is the winner!")