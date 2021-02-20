#################################################################################
# UNION: must use new variable for joining
# UPDATE:  can add to existing variable
#################################################################################

# UNION
set1 = {1,2,3,4}
set2 = {4,5,6,7}
set3 = set1.union(set2)
print(f'add collection using UNION {set3}')

set1 = {1,2,3,4}
set2 = {5,6,7}
set2.union(set1)
print(f'UNION on existing var {set2}, =====>>> it doesnt update')

# UPDATE
set1 = {1,2,3,4}
set2 = {4,5,6,7}
set2.update(set1)
print(f'add collection using UPDATE in exist var {set2}')

#======================================================================================
# Keep ONLY the Duplicates
# intersection_update(), picks common values and stores in EXISTING var
# intersection(), picks common values and stores in NEW var
#======================================================================================
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

#=======================================================================================
#symmetric_difference_update(), method will keep only the elements that are NOT present in both sets.
#symmetric_difference(), method will return a new set, that contains only the elements that are NOT present in both sets.
#=======================================================================================

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
#=======================================================================================

# Difference:
# it returns remaining values in set1 after eleminating comon values
set1 = {1,2,3,4}
set2 = {2,3,5,6}
set3 = set1.difference(set2)
print(f'difference in list {set3}')
