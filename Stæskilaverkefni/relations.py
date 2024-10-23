# T-117-STR1 Discrete Mathematics I
# Template for Individual assignment 5
# R = Relation

# Problem 1a)
def is_reflexive(defined_set, relation_on_set):
    '''
    it's reflexive if all i are represented as (i,i) in the R
    so we simply check for the opposite, and return False if found. 
    Otherwise True
    '''
    for i in defined_set:
        if (i, i) not in relation_on_set:
            return False
    return True

# Problem 1b)
def is_symmetric(relation_on_set):
    '''
    symnetric R is if (y,x) in R then (x,y) 
    must also be in R so we simply check for the opposite, 
    and return False if found. Otherwise True
    '''
    for i in relation_on_set:
        if i[::-1] not in relation_on_set:
            return False
    return True

# Problem 1c)
def is_antisymmetric(relation_on_set):
    '''
    We check for a counter example and return False if found
    So if (x,y) and (y,x) in R and x is not equal to y 
    then return False
    '''
    for i in relation_on_set:
        if (i[::-1] in relation_on_set) and (i != i[::-1]):
            return False
    return True

# Problem 1d)
def is_transitive(relation_on_set):
    '''
    if (x,y) and (y,z) in R then (x,z) must also be in R for this to be true
    so we try to find "counters examples". and Return False if so. 
    '''
    for (x, y) in relation_on_set:
        for (y_2, z) in relation_on_set:
            if y_2 == y:
                if (x, z) not in relation_on_set:
                    return False
    return True

# Problem 2    
def is_equivalence_relation(defined_set, relation_on_set):
    '''
    For there to be equivalence then they should be reflexive,
    R should be synmetric and transitive. 
    We reuse old functions and just do a check for counter examples, if so return False
    Otherwise return True. 
    '''
    if (is_reflexive(defined_set, relation_on_set)) == False:
        return False
    if (is_symmetric(relation_on_set)) == False:
        return False
    if (is_transitive(relation_on_set)) == False:
        return False
    return True

# Problem 3
def composite_relations(relation1, relation2):
    '''
    if (x,y) is in R1 and (y, c) in R2 then (x, c) is composite R
    so we check for the cases where it is true, add them to a list 
    and then return the list after the loop. 
    '''
    comp_list =  []
    for (x, y) in relation1:
        for (y_2, c) in relation2:
            if y == y_2: 
                if (x,c) not in comp_list:
                    comp_list.append((x, c))
    return comp_list

# Problem 4a)
def aces_in_relation_a(A):
    '''
    We imagine A matrix, rows labelled as a, and columms labelled as b. The elements of a and b are the same set of {1,2,3,4,...n}
    so the top left corner of the matrix starts at 1, both row and columm. and goes up the more down and the more to the right we go by 1 each time
    So for each a or "row" we go through the b or "line" and see if there are any b for (a, b) where a equals 0. if so that is counted in our R.
    There are no cases where this is true since our set starts on 1. but lets assume it may be. We use "_" as a placeholder, for repetition use
    A demonstration here, and this is the matrix for all variations of problem4
    b > 1 2 3 4 5 6 7 8 9 ....
    a ↓
      1 (1.1) (1.2) (1.3) (1.4) and so on
      2 (2.1) (2.2) (2.3) (2.4) and so on
      3
      4
    ...
    '''
    R_count = 0
    for a in A:
        for _ in A: 
            if a == 0:
                R_count += 1
    return R_count

# Problem 4b)
def aces_in_relation_b(A):
    '''
    We imagine A matrix, rows labelled as a, and columms labelled as b. The elements of a and b are the same set of {1,2,3,4,...n}
    so the top left corner of the matrix starts at 1, both row and columm. and goes up the more down and the more to the right we go by 1 each time
    So for each a or "row" we go through the b or "line" and see if there are any b for (a, b) where a equals b+1. if so that is counted in our R.
    '''
    R_count = 0
    for a in A:
        for b in A:
            if a == (b+1):
                R_count += 1
    return R_count

# Problem 4c)
def aces_in_relation_c(A):
    '''
    We imagine A matrix, rows labelled as a, and columms labelled as b. The elements of a and b are the same set of {1,2,3,4,...n}
    so the top left corner of the matrix starts at 1, both row and columm. and goes up the more down and the more to the right we go by 1 each time
    So for each a or "row" we go through the b or "line" and see if there are any b for (a, b) where a is more or equal to b. if so that is counted in our R.
    '''
    R_count = 0
    for a in A:
        for b in A:
            if a >= (b):
                R_count += 1
    return R_count
   
# Problem 4d)
def aces_in_relation_d(A):
    '''
    We imagine A matrix, rows labelled as a, and columms labelled as b. The elements of a and b are the same set of {1,2,3,4,...n}
    so the top left corner of the matrix starts at 1, both row and columm. and goes up the more down and the more to the right we go by 1 each time
    So for each a or "row" we go through the b or "line" and see if there are any b for (a, b) where a+b equals 1000. if so that is counted in our R.
    '''
    R_count = 0
    for a in A:
        for b in A:
            if (a+b) == 1000:
                R_count += 1
    return R_count
    
# Problem 4e)
def aces_in_relation_e(A):
    '''
    We imagine A matrix, rows labelled as a, and columms labelled as b. The elements of a and b are the same set of {1,2,3,4,...n}
    so the top left corner of the matrix starts at 1, both row and columm. and goes up the more down and the more to the right we go by 1 each time
    So for each a or "row" we go through the b or "line" and see if there are any b for (a, b) where a+b is more or equals 1001. if so that is counted in our R.
    '''
    R_count = 0
    for a in A:
        for b in A:
            if (a+b) >= 1001:
                R_count += 1
    return R_count