'''
1. Tuple stores any data type
2. Ordered that means indexed
3. *** IMMIUTABLE ****
4. Allow duplicates

NOTE: When tuple is used... When a list required that doesn't accept immutable values.
'''
tpl = (1,2,'Srujan',1,False)
#print(tpl[0], tpl[3])

# =====================================
# change from tuple to List without chnaging values & variable.

tpl_lst = (1,2,3)
#print(type(tpl_lst))
tpl_lst = list(tpl_lst)
#print(type(tpl_lst))

# ======================================

del tpl_lst
#print(tpl_lst)

# =======================================

fruits = ("apple", "banana", "cherry")

fresh = [a for a in fruits]
#print(fresh)

# ======================================

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
lst = []
[f, *fruit_basket] = fruits

#######################################################
# TUPLE is immutable so we can join into a new tuple.
# LIMITATIONS: at least 2 elements in each tuple to concatinate
#######################################################

tpl = (5,4)
tpl2 = (2,3)
tpl3 = tpl + tpl2
print(tpl3) # addition

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)







