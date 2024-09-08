# Inverse Case

#Tökum streng, förum í gegnum hann einn staf í einu. 
# breytum stafnum í ASCII tölu og kíkjum hvort hann sé 65-90(hástafir)
# eða 97-122(lágstafir) og + eða - 32 eftir stöfum/tölum
# svo breytt aftur í stafi en ekki ASCII numer 
# ef þetta er ekki inn í þessu range-i þá er ekkert gert við stafin

strengur = input()
new_strengur = ""

for letter in strengur:
    ASCII_numer = ord(letter)
    if ASCII_numer >=65 and ASCII_numer <= 90:
        ASCII_numer += 32
        new_strengur += chr(ASCII_numer)
    elif ASCII_numer >=97 and ASCII_numer <= 122:
        ASCII_numer -= 32
        new_strengur += chr(ASCII_numer)
    else:
        new_strengur += chr(ASCII_numer)
print (new_strengur)

#Optmize
# Það er hægt að gera þetta mun skilvirkara með swapcase function
strengur = input()
new_strengur = strengur.swapcase()
print(new_strengur)

#Optimize.is
print(input().swapcase())