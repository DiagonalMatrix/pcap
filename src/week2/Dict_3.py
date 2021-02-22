####################################################################
# Unlike LIST object, Pop only accepts key NOT INDEX values eg: pop(0)
# popItems behaves as pop in List object
# until 3.7, a popitem removes random item.
####################################################################

dict = {'name':'Srujan',
        'id': [1,2,3],
        'postcode': 100,
        'locaion':'reading'}

dict.pop('name')
#print(f'Th pop function is {dict}') # {'id': [1, 2, 3], 'postcode': 100, 'locaion': 'reading'}
dict['postcode']=101
dict.popitem()
#print(f'Th popitems() function is {dict}') #{'id': [1, 2, 3], 'postcode': 101}

# ================================================
dict = {'name':'Srujan',
        'id': [1,2,3],
        'postcode': 100,
        'locaion':'reading'}

for elm in dict:
    print(f'Element of Dict value is {elm}') # ===============>>>> this retuns only key. =======================
    print(f'{elm} value is {dict[elm]}')

# ========== Print key, Value if used items() object ===============
print('========== Print key, Value if used items() object ===============')

for k,v in dict.items(): # ===============>>>> items retuns list of tuples in a k,v pair. =======================
    print(f'The key is {k} and the value is {v}')


# ========== Dict Copy =================================
print('# ========== Dict Copy =================================')

dict1 = dict.copy()
print('Copied print object is ',dict1)

# ===================== Nested Dictionary ===================================
print('# ===================== Nested Dictionary ===================================')
# 2 Ways to craete a dictionary

# Method 1:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Method 2:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print('Parent hierarchy',myfamily)

for child, dtls in myfamily.items():
    print(f'the child=====>>>> {child} is and the details are details {dtls} ')
    for key, value in dtls.items():
        print(f'the key is {key} and the values are {value}')


