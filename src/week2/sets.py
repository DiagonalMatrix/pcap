############################################################
# Set is one of 4 built-in data types in Python (List, Set, Tuple, Dictionary)
# Accepts any data types
# No duplicates, unordered and unindexed (Can't use index set[0]).
# immutable
# Can't add List & Dict becz they are mutable, only imutable eg: Tuple
############################################################


tpl = (1,2,3)
t1 = ('Srujan',1)
set1 = {True,1,2,'Srujan','Ram','Ramesh',False,0,True,tpl,t1}
# True,2,Srujan, Ram,Ramesh,False,Tpl
# False,Ram,ramesh,Srujan,True,tpl
# {False, True, 2, (1, 2, 3), 'Srujan', 'Ramesh', 'Ram'}
print(set1)

# Does Set accepts Boolean values?
'''
NOTE:
1. If your set has 0 & False, it only take one value.
2. becz False and 0 are same becz doesn't accept duplicates 
'''
b1 = (True,False, True, False)
s1 = {b1}
sets1 = {True, False, 2}
#print(sets1)

# Order of sequence
# NOTE: in BOOL If numeric is the first element, it takes numeric only and ASC same datatype while priting
# otherwise, there is no specific order of display for other datatypes, and displays randomly.
set = {True,1,False,0} # {False, True}
set = {1,True,0,False}
print(set)



