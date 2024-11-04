# Hail Caesar!
import sys

decrypted = []
flag = True
for encrypted_string in sys.stdin:          
    if flag:                              
        first = ord(encrypted_string[0])    
        shift = first-72                    
        flag = False                       
    for letter in encrypted_string:         
        if letter == "\n":
            decrypted.append(letter)
        else:
            shifted = ord(letter)-shift
            if shifted < 32:                       
                shifted = 126 - (31 - shifted)
            elif shifted > 126:
                shifted = 32 + (shifted -127)
            decrypted_letter = chr(shifted)

            decrypted.append(decrypted_letter)
    
decripted_sentance = ("".join(decrypted))
if decripted_sentance[-1] == "\n":
    decripted_sentance = decripted_sentance[:-1]

print (decripted_sentance)