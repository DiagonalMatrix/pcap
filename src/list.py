# List by default takes dictionary keys unless values() specified.
d = {'a':1,'b':2}
l = list(d)
#print(l)

# element check in list object
a = 1
b = [1,1,2]
if a in b:
    print(a)

# Insert() requires an Index & value.
lst = [1,2,3]
lst.insert(1,'srujan') # [1, 'srujan', 2, 3]

# Append doesn't requires Index
lst = []

for a in range(5):
    lst.append(a)

llst = ['a']
llst.append('b')
#print(llst)

lst1 = [1,2,3]
lst2 = [4,5,6]
lst1.append((4,5,6)) # [1, 2, 3, (4, 5, 6)]

# ========== EXTEND ==================
lst1 = [4,5,6,7]
lst2 = [8,9,10,11]
lst1.extend(lst2) #[4, 5, 6, 7, 8, 9, 10, 11]

