#Square, but Not the Math Kind
number = int(input())

for i in range(0,number):               
    for x in range(0, number):          
        if i == 0 or i == number-1:     
            if x < number-1:            
                print ("* ", end="")
            elif x == number-1:         
                print ("*", end="")
        elif x == 0:                   
            print ("* ", end="")
        elif x == number-1:             
            print ("*", end="")
        else:                          
            print ("  ", end="")
        
    print ()                            