# Tarifa

# Við eigum að gera talningarforrit, sem tekur við 2 heiltölu input breytum til að byrja með, einnig gerum við total breytu með gildi 0
# fyrsta er takmarkið á neti sem notandi fær að nota í hverjum mánuði, seinni er hve marga mánuði við erum að reikna út frá. 
# hann má nefnilega færa það sem er ekki notað yfir í einhverskonar banka til að nota síðar. 
# við notum for range loopu með fjölda mánuði breytuni til að stjórna stærð á loopinu og spyrjum notanda hversu mikið hann notaði á hverjum mánuði
# við notumst við heiltölu input breytu í loopinu til að gera þetta, svo tökum við gildi sem slegið er inn og mínusum það frá takmarkinu sem hann-
# fær á hverjum mánuði. afgangurinn af því er svo bætt við total breytuna. 
# eftir að loopið er búið þá plúsum við einn mánuð virði af takmarki við total breytuna ig að lokum prentum við út totalið. 


monthly_limit = int(input(""))
number_of_months = int(input(""))
total = 0

for i in range(0, number_of_months, 1):             # byrja á 0, upp í number of months, 1 skref í einu
    used_this_month = int(input(""))                #spyrjum hversu mikið var notað í þessum  mán 
    total += (monthly_limit-used_this_month)        # mínus frá takmarki og afgangi bætt við total

total += monthly_limit         # plúsum eitt takmark við total, því við erum núna í nýjum mánuði og þurfum heildarfjölda sem hann getur nota

print (total)               # prentum total
#Virkar í kattis