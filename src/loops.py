'''
 Remove & Pop in List
 - For remove, mention element.
 - Pop() mention Index
, if none mentioned removes last element.
'''

lst = [10,20,30,40,50,60,70,80,90]
lst.remove(30)
print(lst) # [10, 20, 40, 50, 60, 70, 80, 90]

lst = [20,30,20,40]
lst.remove(20)
print(f'Duplicates in list {lst}') # doesn't concern about duplicates.. only 1st matching element get removed.

lst.pop(0)
print(lst) # [20, 40, 50, 60, 70, 80, 90]

lst.pop()
print(lst) # [20, 40, 50, 60, 70, 80]

# ======================================================

'''
del: removes entire list unless an element is mentioned.
'''

lst = [1,2,3]
del lst[1]
print('Del..',lst)

llst = [11,22,34]
#del llst
print('Where is del???..',llst)

# ========================================================
#  'Clear' deletes all elements in the list
# ========================================================
lst = [10,20,30]
lst.clear()
print(lst)

# =============================================

# list comprehension
lst=[1,2,3,4,5,5,6]
for a in lst:
    print(a)

thislist = ["apple", "banana", "cherry"]
#[print(x) for x in thislist]

# =========================================
fruits = ['apple','banana','grape']
newList = [a for a in fruits if a != 'orange']
#print(newList)

llst = ['hello' for a in fruits]
print(llst)

# ==========================================

new_list = [a if a == 'tomatow' else a for a in fruits]
print('else  ',new_list)

# =========================================
'''
1. Sort().. Asc/Desc
2. Sort is case insensitive. (treats Caps/small as same)
3. Default is Asc unless mentiopned sort(reverse = True)
'''

rev_list = ['Srujan','Ramesh', 'Ram']
rev_list.reverse()
print(rev_list) #['Ram', 'Ramesh', 'Srujan']

# ==========================================

