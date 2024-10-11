#Tok Tik

tok_tik = {}

total_count = int(input())

for counter in range(total_count):
    tik_tokker = input()
    parts = tik_tokker.split(" ")
    key = parts[0]
    value = int(parts[1])
    if key in tok_tik:
        tok_tik[key] += value
    else:
        tok_tik[key] = value

print(max(tok_tik, key = tok_tik.get))
