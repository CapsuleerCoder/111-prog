#Hitastig

input()

numera_setning = input()

numera_setning = numera_setning.split(" ")

numera_listi = []

for word in numera_setning:
    numera_listi.append(int(word))

max_number = max (numera_listi)
min_number = min (numera_listi)
print (max_number, min_number)


