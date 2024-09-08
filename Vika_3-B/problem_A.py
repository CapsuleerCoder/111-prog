# count occurences
# tekur við streng og bókstaf, fer í gegnum allan strenginn einn staf í einu
# ef stafur er jafnt og bókstafur frá notanda þá prentast hvaða index það er í. 

strengur = input()
bókstafur = input()        

for i in range(len(strengur)):
    if strengur[i] == bókstafur:
        print (i)

#Optimized
#sami kóði, enumerate gerir sama og for loopan í þessu tilfelli, i er index count. 
s=input()
b=input()
for i, c in enumerate(s):
    if c == b:
        print(i)