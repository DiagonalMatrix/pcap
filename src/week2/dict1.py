##########################################################################
# store multiple values as key:value pairs.
# ordered*(from 3.7), changeable, duplicates.
# If duplicate keys, values will overwrite with latest/recent values
##########################################################################

dict = {'name':'Srujan',
        'id': [1,2,3],
        'postcode': 100}
print(dict)

#=========== 1st way to access keys ================
name = dict['name']
print(f'Name key value is {name}')

# display single value of a key
ind_val = dict['id'][1]
print(f'first value of id key {ind_val}')

length_dict = len(dict)
print(f'Lenghth of the dict {length_dict}')

#=========== 2nd way to access keys ================
print('#=========== 2nd way to access keys ================')
name = dict.get('name')
print(f'Name key value is {name}')

# display single value of a key
ind_val = dict.get('id')[1]
print(f'first value of id key {ind_val}')

#============ Print all Keys & Values =========================
print('#============ Print all Keys & Values =========================')
dict_keys = dict.keys()
dict_val = dict.values()
print(f'Dict keys are {dict_keys}')
print(f'Dict values are {dict_val}')

#============ Access key values in a loop =========================
print('Access keys in a loop ')
dict = {'name':'Srujan',
        'id': [1,2,3],
        'postcode': 100}

for key_itr in dict:
    val = dict[key_itr]
    print(val)
