#Hipp Hipp Húrra

#Við ætlum að gera forrit sem hrópar hiphop húrra fyrir hvert ár sem viðkomandi hefur verið lifandi og bætir svo nafni notanda við enda strengin
#Við byrjum á því að taka við strengja breytu frá notanda með input og einnig tökum við heiltölu breytu með input frá notanda
#síðan notum við for loop sem fer í gegnum range á aldri notanda og prentar út "Hipp hipp hurra, [nafn]" jafn oft og ár í aldri. 

name = input("") # þetta er strengur sjálfkrafa, má ekki vera skilaboð í þessu þar sem kattis er drasl
age = int(input("")) # við breytum þessu input í int eða heiltölu

for i in range(0, age, 1):  # við gerum for loop með 0 start, age sem enda og hoppum 1 í einu. Age er ekki talin með en þar sem við byrjum að telja á 0 skiptir það ekki öllu
    
    print (f"Hipp hipp hurra, {name}!") # fyrir hvert hopp sem við tökum þá prentum við þetta einu sinni, samtals ætti þetta að prentast út jafn oft og age.
    #print (i+1)  # notum þetta til að prófa hversu oft þetta er að runna, commentum þetta svo út 


#Virkar í Kattis


