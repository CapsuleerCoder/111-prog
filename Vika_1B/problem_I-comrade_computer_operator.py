#Comrade Computer Operator

new_temp  = int(input())
old_temp  = int(input())

if new_temp >= 350:
    print ("shutdown")
elif new_temp < 300 and new_temp <= old_temp:
    print ("raise")
elif new_temp < 300 and new_temp >= old_temp:
    print ("keep")
elif new_temp == 300:
    print ("keep")
elif new_temp > 300 and new_temp >= old_temp:
    print ("lower")
elif new_temp > 300 and new_temp <= old_temp:
    print ("keep")