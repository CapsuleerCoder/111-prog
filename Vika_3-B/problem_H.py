#Pig Latin

#fékk þetta ekki að virka með öðru en sys.stdin
#geri lista til að fylla af með orðum fyrir breytingu. Það er gert í for sys.stdin strengum. 
# Svo förum við í gegnum lista, línu fyrir línu, orð fyrir orð og skoðum hvort það sé sérhljóði eða ekki
# og bætum yay eða ay við og færum til orðið aðeins og bætum í nýjan lista. 
# Setjum svo \n new line ef þetta er síðasta orð í línunni
# Annars bara space og svo endum við með að prenta þetta allt úr þessum nýja lista 

import sys

listinn = []
counter = 0
vowels = ["a", "e", "i", "o", "u", "y"]
sentance = []

for strengur in sys.stdin:
    strengur = strengur.strip()
    if strengur:
        strengur = strengur.split()
        listinn.insert(counter,strengur)
        counter += 1


for line in listinn:
    for index, word in enumerate(line):
        flag = False
        if word[0] in vowels:
            sentance.append(word +"yay")
        else:
            for letter in range(len(word)):
                if word[letter] in vowels and not flag:
                    sentance.append(word[letter:] + word[:letter] + "ay")
                    flag = True
        if index ==len(line) -1:
            sentance += "\n"
        else:
            sentance += " "

print ("".join(sentance))