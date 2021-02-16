import pandas as pd
# BOOL evaluates TRUE except 0 and EMPTY
b1 = 'srujan'
b2 = 'Ramesh'
print(bool(b1)==bool(b2)) # compares DataTypes, not the VALUE

b11 = 100
b12 = 100
print(bool(b11)==bool(b12))

b11 = 100
b12 = 120
print(bool(b11)==bool(b1))

non_empty = ''
zero = 0
values = '123'
nulls = None
print(bool(non_empty),bool(zero),bool(values),bool(nulls)) # False False True False

# ================== Exercise
pd.options.display.width = 0
#df = pd.read_csv('/home/srujan/Desktop/sample.csv')
df = pd.read_excel('/home/srujan/Desktop/sample.xls')
print(df)
print('=====================================')
df = df.fillna('', inplace=True)
print(df)


# =========== ISINSTANCE ==========

a = 100
b = 'srujan'

print(isinstance(a, int))
if type(a) == type(b) and a == b:
    print('Both matched')
else:
    print('Not Matched')
