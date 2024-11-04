#Elo Rating

elo = int(input())

if elo >= 2700:
    print("Super grandmaster")
elif elo >= 2500:
    print("Grandmaster")
elif elo >= 2400:
    print("International grandmaster")
elif elo >= 1000:  
    print("Amateur")
else:
    print("Invalid")