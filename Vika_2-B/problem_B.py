#Countdown

# Við eigum að gera forrit sem tekur við int eða heiltölu og telur frá henni og niður í einn þar sem hún á að hætta. 
# Þá byrjum við að taka við einni heiltölu með input frá notanda
# Gerum svo for loop sem fer í gegnum þetta frá input notanda og niður í 0 með -1 í hoppi og prentar alltaf í hverri lykkju i töluna 

number = int(input("")) # tökum við heiltölu 

for i in range(number, 0, -1):   # gerum for lykkju sem byrjar í number, endar í 0(en þar sem 0 er ekki talið með er þetta að enda í 1) og tekur -1 hopp í hverri lykkju
    print (i) # prentum i í hvert sinn, ættum þá að fá niðurtalningu í hvert sinn


# Virkar í katiss




















