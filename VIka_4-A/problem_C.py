# Extracting a Number

# Gerum tóma strengjabreytu, eitt stykki flagg og förum svo í gegnum strenginn,
#  ef hann er tala þá er hann bættur við tómu strengjabreytuna og sett flaggið upp. 
# Ef hann fer svo í staf sem er ekki tala þá kíkir hann hvort strengjabreytan sé tóm
# og hvort flaggið er uppi, ef svo er þá er sent til baka strengjabreytan breytt í int 
# ef þetta fer allt í gegn og strengjabreytan er ekki tóm þá er hún send til baka einnig
# annars er -1 sendur til baka

def extract_first_number_from_string(string_to_search):
    string_to_change = ""
    flag = False
    for letter in string_to_search:
        if letter.isdigit():
            string_to_change += letter
            flag = True
        elif flag and string_to_change:
            return int(string_to_change)
    if string_to_change:
        return int(string_to_change)
    return -1


# Er hægt að taka flaggið út en ekki mikið meira en það. 

def extract_first_number_from_string(string_to_search):
    string_to_change = ""
    for letter in string_to_search:
        if letter.isdigit():
            string_to_change += letter
        elif string_to_change:
            return int(string_to_change)

    return int(string_to_change) if string_to_change else -1
