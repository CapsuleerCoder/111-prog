# Hail Caesar!
import sys

decrypted = []
flag = True



for encrypted_string in sys.stdin:          # notum stdin þar sem það eru margar línur
    if flag:                                # Kikjum hversu mikið shift við þurfum
        first = ord(encrypted_string[0])    
        shift = first-72                    # vitum að fyrsti er alltaf stór H sem er 72 í ASCII
        flag = False                        # Ef flag þá fer þetta ekki aftur í gang
    for letter in encrypted_string:         #Fer í gegnum alla stafi, ef new line þá ekkert annars er þetta shiftað
        if letter == "\n":
            decrypted.append(letter)
        else:
            shifted = ord(letter)-shift
            if shifted < 32:                        # Passað upp á að þetta fari ekki out of bounds með wrappi
                shifted = 126 - (31 - shifted)
            elif shifted > 126:
                shifted = 32 + (shifted -127)
            decrypted_letter = chr(shifted)

            decrypted.append(decrypted_letter)
    

decripted_sentance = ("".join(decrypted))
if decripted_sentance[-1] == "\n":
    decripted_sentance = decripted_sentance[:-1]

print (decripted_sentance)

