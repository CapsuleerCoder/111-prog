
encrypted_string = input("")

decrypted = ""

for char in encrypted_string:
    shifted_char = chr(ord(char) - 5)
    decrypted += shifted_char

print(decrypted)