# Adding new element to Keys

dict = {'name':'Srujan',
        'id': [1,2,3],
        'postcode': 100}

dict['location'] = 'Reading'
print(dict)
# {'name': 'Srujan', 'id': [1, 2, 3], 'postcode': 100, 'location': 'Reading'}

dict['name'] = 'Ram'
# {'name': 'Ram', 'id': [1, 2, 3], 'postcode': 100, 'location': 'Reading'}
print(dict)

# ============= DICT iTEMS ===================

dict_itms = dict.items()
print(f'Dict Items are {dict_itms}')

# Returns:
# List of Tuples
#([('name', 'Ram'), ('id', [1, 2, 3]), ('postcode', 100), ('location', 'Reading')])

# ================ CHECK IF KEY EXISTS IN DICT==============================

if 'name' in dict:
    print('====== NAME in dict')
    print(dict['name'])

# ================ items() =============================
print(f'items contains === >>> {dict.items()}') # returns list of Tuples

for key, val in dict.items():
    print(f'The kay is {key} and the value is {val}')


# ========== UPDATE ======================
#NOTE: I didn't see any diff in below 2 formates.

dictin = {'id': 100,
          'year': 2020}

# Method 1
dictin.update({'year':2021})
dictin.update({'name':'Srujan'})

# Method 2
dictin['serial'] = 12345

