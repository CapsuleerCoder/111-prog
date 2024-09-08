# Email addresses
#leiðinda verkefni. Ógeðslega langur if og elif texti. 
email = input()
email = email.strip()
flag = True
position = email.find("@")

while flag:
    if not "@" in email:
        print ("@ symbol is missing.")
        flag = False
    elif email.count("@") > 1:
        second = email.find("@", position+1)
        print (email) 
        print (" "*(second-1),"^--there is an extra @ symbol here.")
        flag = False
    elif email[0] == "@":
        print ("There is nothing before the @ symbol.")
        flag = False
    elif email[(len(email)-1)] == "@":
        print (email)
        print (" "*(len(email)-1), "^--there is nothing after the @ symbol.")
        flag = False
    elif email[0] == ".":
        print ("Email address starts with a dot.")
        flag = False
    elif email[position-1] == ".":
        print (email)
        print (" "*(position-2),"^--there is an extra dot here.")
        flag = False
    elif ".." in email:
        double = email.find("..")
        print (email)
        print (" "* (double-1), "^--there are consecutive dots here.")
        flag = False
    elif not email.endswith(".is"):
         print ("Top-level-domain is missing.")
         flag = False
    else:
        print ("All good.")
        flag = False