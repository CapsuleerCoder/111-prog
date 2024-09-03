#Square, but Not the Math Kind

#Við eigum að skrifa forrit sem tekur við int input frá notanda og smíðar ferhyrning úr honum úr * merkjum 
# ef notandi skrifar 5 þá ætti ferhyrningurinn að vera 5x5 og svo framleiðis. 
#aðeins ytri lag ferhyrningings ætti að hafa * merki, rest ætti að vera tómt. Einnig er krafa að engin lína má enda á bili. 

number = int(input())


for i in range(0,number):               # i er línunar, i er fyrsta lína til lína numer (number)
    for x in range(0, number):          # x eru stafinir á línunni
        if i == 0 or i == number-1:     # ef þetta er fyrsta lína eða lína 0 eða síðasta lína (number-1) þar sem range fer upp að en ekki í number
            if x < number-1:            # ef x sem er stafir á línu er ekki síðasti stafurinn í línnuni þá prentar hann * með bili
                print ("* ", end="")
            elif x == number-1:         # ef x sem er stafur á línu er síðasti eða number-1 út af range þá prentar hann bara * því það má ekki enda á bili
                print ("*", end="")
        elif x == 0:                    # ef x er ekki fyrsta eða síðasta lína þá fer þetta í gang og kíkjir á hvort þetta sé fyrsti stafur í línu, þá prentast * með bili
            print ("* ", end="")
        elif x == number-1:             # ef x er síðasti stafur í línu þá prentast bara stjarna. 
            print ("*", end="")
        else:                           # annars prentast bara tvöfalt bil 
            print ("  ", end="")
        
    print ()                            # síðan prentum við eftir hverja línu , gætum einnig sett \n í end á öllum stöðum þar sem bara * er prentuð. 
    
#virkar í kattis
