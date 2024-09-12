#Lexicographical Order

# Frekar einfalt, tekur tveir strengjabreytur, breytir þeim í lowercase með lower() 
# Metur hvor er minni og return honum 

def precedes(one_string, another_string):
    if one_string.lower() < another_string.lower():
        return (one_string)
    else:
        return (another_string)

precedes(input(), input())