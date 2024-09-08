# Every other letter
#Tökum streng, gerum lista, fyrir hvert stak í streng þá förum við yfir það
# skoðum hvort það deilist með með 0 afgang(slett tala), ef svo er set í listan
# enda með að prenta streng sem listin fer í 
strengur = input()
new_strengur = []

for i, c in enumerate(strengur):
    if i % 2 == 0:
        new_strengur.append(c)
print ("".join(new_strengur))


# Optimized

# augljósalega betra að nota slice

s=input()
print(s[::2])
