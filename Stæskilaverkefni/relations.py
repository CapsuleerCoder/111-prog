# T-117-STR1 Discrete Mathematics I
# Template for Individual assignment 5

'''
R = relation

'''

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
    
    return 

# Problem 4a)
def aces_in_relation_a(A):
    return #TODO Implement

# Problem 4b)
def aces_in_relation_b(A):
    return #TODO Implement

# Problem 4c)
def aces_in_relation_c(A):
    return #TODO Implement
   
# Problem 4d)
def aces_in_relation_d(A):
    return #TODO Implement
    
# Problem 5e)
def aces_in_relation_e(A):
    return #TODO Implement


print ()