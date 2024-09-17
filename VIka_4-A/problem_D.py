#Range Sum

# tökum inn þetta range, förum í gegnum það með for in range lykkju og bætum öllu við summu og returna henni svo
# endapunktur er með +1 því hann er inclusive.  

def sum_of_range(start, end, step):
    sum = 0
    for i in range(start,end+1,step):
        sum += i
    return sum


# er hægt að gera þetta aðeins styttra með innbyggðu falli

def sum_of_range(s,e,i):
    return sum(range(s,e+1,i))