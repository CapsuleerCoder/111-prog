#Subaruba

import sys
#Subaruba uber skrubytubin.


#Get svo sem farið í gegnum þetta allt í einu og bara gert eitthvað ef
# vowel og before vowel er sama. 
# EF svo er get ég sliceað allt og tekið bara þann part í burtu

#Sara er skrytin.

#S "ub" a r "ub" a
listinn = []
vowels = ["a", "e", "i", "o", "u", "y"]
index_list = []
decrypted_sentance = []
count = 0
decrypted_word = []
for line in sys.stdin:
    # if a:
    # int ignore
    listinn = line.split()
    for word in listinn:
        for index in range(len(word)):
            if word[index] in vowels and (word[index-2:index] == "ub"):
                index_list.append(index)


            for i in index_list:
                decrypted = word[count:i-2]
                if i == index_list[-1]:
                    decrypted = word[i:]
                decrypted_word.append(decrypted)
                count = i

            print (decrypted_word)
            decrypted_sentance.append(decrypted_word)
            decrypted_word = []
            index_list = []
            

print ("".join(decrypted_sentance))
                