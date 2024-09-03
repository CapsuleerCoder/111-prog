#Triangular Numbers

# Verkefnið er að gera forrit sem tekur við number eða heiltölu input frá notanda og  einnig total breytu með gildið 0 
# Við þurfum að plúsa allar tölur sem telja upp í number í totalið, talan sjálf talin með einnig
# Við gerum þetta í for lykkju með range sem fer upp í number+1 og frá 1, því annars stoppar lykkjan áður en hún kemst alla leið í töluna sjálfa. 
# hverri lykkju þá plúsum við lykkju-breytuna í lykkjuni við totalið og prentum totalið sem komið er so far. 

number = int(input(""))

total = 0

for i in range(1, number+1, 1):    # byrjum á 1, skiptir svo sem engu en óþarfi að byrja á 0, endum á tölunni+1 og tökum eitt skref í einu
    total += i                     # plúsum svo hvert skref í totalið
    print (total)                  # prentum total í hverju skrefi


#virkar í kattis