#Decimal to Binary

# Þetta er frekar gefið dæmið með lýsingu sem kemur með en við gerum breytum decimal í int til þess að hafa það alveg á hreinu. 
# gerum lista, gerum snökkt check hvort það sé verið að skítachecka okkur með 0 og svörum þá bara 0 til baka
# förum svo í gegnum decimal eina deilingu með 2 í einu. tökum remainder og setjum það fremst í listan sem streng sem við gerðum
# breytum svo decimal í niðurstöðu heiltöludeilingar með 2 
# á endanum prentum við út listann í str formi


def decimal_to_binary(decimal):
    decimal = int(decimal)
    binary_list = []
    if decimal == 0:
        binary_list.insert(0, str(0))
    while decimal != 0:
        remainder = decimal % 2
        binary_list.insert(0, str(remainder))
        decimal = decimal // 2
    return ("".join(binary_list))


#print(decimal_to_binary(input()))


# Þetta er einnig önnur leið, gert bara streng beint.

def decimal_to_binary(decimal):
    binary_streng = ""
    decimal = int(decimal)
    if decimal == 0:
        binary_streng = "0"
    while decimal != 0:
        binary_streng = str(decimal % 2) + binary_streng
        decimal = decimal // 2
    return binary_streng