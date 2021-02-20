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
