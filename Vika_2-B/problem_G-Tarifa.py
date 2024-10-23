# Tarifa

monthly_limit = int(input(""))
number_of_months = int(input(""))
total = 0

for i in range(0, number_of_months, 1):             
    used_this_month = int(input(""))                
    total += (monthly_limit-used_this_month)        

total += monthly_limit   

print (total)             