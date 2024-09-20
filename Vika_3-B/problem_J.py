#Subaruba

import sys

#Sara er skrytin.

#S "ub" a r "ub" a


# Ég hugsa að það sé best að setja þetta allt í lista, per línu og svo per word, svo taka það í sundur í per staf
# Fara svo í gegnum stafina, ef vowel finst þá adda ub fyrir framan. 
# TIl að decodea þá geri ég svipað nema tek fyrstu 2 fyrir framan ef vowel finnst. 


listinn = []
vowels = ["a", "e", "i", "o", "u", "y"]
working_list = []
count = 0
end_result = []
work_string = ""

for line in sys.stdin:
    line = line.strip()
    if line:
        line = line.split()
        listinn.insert(count, line)
        count += 1

for line in listinn:
    for word in line:
        for i in word:
            working_list.append(i)
        for index in range(len(working_list)):
            if working_list[index] in vowels:
                working_list.insert(index, "ub")
            
        for letter in working_list:
            work_string = work_string.join(letter)
print (work_string)



            

#print ("".join(decrypted_sentance))
                