#Sum of Powers 

# Í þessu vandamáli eigum við að taka við tveimur input breytum til að byrja með, það er base tala, og svo er það fjöldi af tölum 
# við gerum líka total breytu með gildinu 0, allar tölur í röðinni verða base talan
# eftir að við fáum þessar 2 tölur þá gerum við for range loop með fjöldan af tölum sem range-ið. 
# í hverji loopi þá spyrjum við notandan hvaða veldi hann vilji að næsta base talan í röðinni sé. 
# síðan setjum við base töluna í veldið sem er beðið um, plúsum niðurstöðina í totalið og næsta lykkja fer í gang. 
# eftir að lykkjan er búin þá prentum við út total

base_number = int(input(""))
length_number = int(input(""))

total = 0

for i in range(0, length_number, 1):        #byrjar í 0, fer upp í length_number-1 og eitt skref í einu. 
    exponent = int(input())                 # biðjum um veldi
    total += (base_number**exponent)        # hífum base number upp í veldið sem valið far og plúsum það við totalið. 

print (total)


#Virkar í kattis