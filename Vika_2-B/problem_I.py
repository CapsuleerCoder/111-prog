#Sine Wave
#Eigum að teikna upp sine wave með X-um
#Nota á tvær breytur, N sem stjórnar hversu margar bylgjur/waves það eru og L sem stjórnar hversu margar línur eru prentaðar
#Við setjum formulu sem er gefin af Kattis inn til að finna hversu marga radians á hverri línu eiga að vera
#notum svo 


import math

N = int(input())
L = int(input())

radians_each_line = (2 * math.pi * N) / L            # þetta er formula sem kemur með dæminu

for i in range(L):

    x_count = round(20 * (math.sin(i* radians_each_line) + 1))    # við margföldum línuna við radians formulu, plúsum einn við og fáum svo sin úr því, margföldum með 20 eða semi amplitude og roundum þetta til að fá ekki mínus tölu
    print ("x"*x_count)         # svo prentum við út eins mörg x og við fáum úr formúlunni á undan


#virkar í kattis