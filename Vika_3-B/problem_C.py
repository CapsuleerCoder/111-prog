# Formatting
#Tökum float tölu frá notanda. Prentum hana svo út með format
# ":" er format ">" er right justified, 12 er field width, 
# f er fixed point notation til að fá tölu sem er skiljanleg
# 2 er hversu mikið af aukastöfum við viljum. 
number = float(input())
print(f'{number:>12.2f}')

# Optimized
# ekki hægt að gera mikið, getur stytt breytu nöfn og
# gert þetta allt í einni línu en það bætir ekkert, skemmir bara læsileika
n=float(input())
print(f'{n:>12.2f}')
