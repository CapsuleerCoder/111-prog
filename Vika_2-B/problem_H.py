#Sum of Digits

# Eigum að gera forrit sem tekur við heiltölu runu, t.d. "1582252523", plúsar svo hverja tölu í rununni saman og prentar total. 
# Við byrjum á að gera input breytu og total breytu með gildi 0. 
# Notum svo modulus til að fá aftasta staf og plúsum hann við total, notum svo heiltöludeilingu til að losna við aftasta staf. 
# prentum total eftir að lykkjan klárast


number = int(input())
total = 0

for i in range(len(str(number))):              # Við þurfum að breyta þessu í str til að finna hversu langt þetta er
    remainder = number % 10                    # síðan deilum við með 10 og finnum afganginn sem er síðasti stafur. 
    total += remainder                        # plúsum afganginn við total
    number = number // 10                      # heiltöludeilum orginal tölunni niður um tíu til að losna við aftasta staf 
    print (number)

print (total)

#Virkar í kattis