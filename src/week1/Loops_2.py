'''
1. Loops won't copy elemnts, instead port to another list eg: list1 = list2
2. If any changes occured in right side list, those reflects in left side list.
3. hence explicit copy() is required.
'''

lsit1 = [0,1,2,3,44]
lst2 = lsit1.copy()

lsit1.append(70)
#print(lst2)
#print(lsit1)

# =============================================
# Join list in 3 ways

l1 = [10,20]
l2 = ['srujan',40]

Method1 = l1 + l2
print(Method1)

# method 2:
for method2 in l1:
    l2.append(method2)
print('Method 2',l2)

l1.extend(l2)
print('Extend',l1)

l1.append(l2)
print('list in the list', l1)

# ==================================
