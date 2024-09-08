# Palindrome

#Tökum streng frá notanda
#Berum hann saman lesin frá vinstri við hann lesin frá hægri
# ef svo er prenta palindrome ef ekki þá prenta nei

strengur = input()

if strengur[::1] == strengur[::-1]:
    print ("Palindrome!")
else: 
    print ("Nothing special about this string :(")


#Optimized
# Hérna er hægt að gera þetta mun smærra en græðir ekkert á þessu og þetta skemmir læsileika
print("Palindrome!" if (s := input()) == s[::-1] else "Nothing special about this string :(")
