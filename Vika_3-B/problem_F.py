# Format Name

#Tökum við streng, finnum index á "," notum það svo til að prenta fyrsta staf eftir ","
# og svo slice af strengnum upp að ",". 

strengur = input()

position = strengur.find(",")

print(f"{strengur[position+2].upper()}. {strengur[:position].capitalize()}")


#Optimized 
#Ekki hægt að gera mikið meira án þess að virkilega skemma læsileika