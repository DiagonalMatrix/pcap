##############################################################
# 1. you can add new elements
# 2. you can use add/Update
##############################################################

# Add: is used to add single element only
set = {1,2}
set.add(3)
print('New elem added ',set)

#Adding Collection: adding collection using add method
set = {1,2}
col = {3,4,5,6}
set.update(col)
print(f'updating with collection {set}')

set = {1,2}
lst = [4,5,6,7]
set.update(lst)
print(f'adding list collection {set}')

##############################################################################
# 1. Remove(): Remove elemt, thropws error if elemt  not present.
# 2. discard(): Removes element, 'DOESNT' through error if elemt not present.

#NOTE: Advisable to use discard() to avoid error at run time.
##############################################################################
rm1 = {'Srujan','Ramesh','Ram'}
rm1.remove('Srujan')
print('Remove using remove() ',rm1)
#rm1.remove('Srujan')

rm1 = {'Srujan','Ramesh','Ram'}
rm1.discard('Srujan')
rm1.discard('Srujan')
print(f'remove using discard{rm1}')


##############################################################################
# 1. Pop(): Removes last elemt, unlike list no idex possible hence default last elmt removed
# 2. clear(): Clears all elmnt
# 3. del: deletes variable completely.
##############################################################################
