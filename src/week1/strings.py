a = 'Hello World'
#print(len(a))


for ram in range(len(a)):
    #print(a[ram])
    None

# String is considered as Array hence no need to convert as a collection.
for ii in a:
    #print(a[ii])
    None


# search for a string in a string
# this is a case sensitive
a = 'reading'
txt = 'I live in Reading!'

res = a.lower() in txt.lower()
#print(res)

# If consition
if a in txt:
    #print('It is present')
    None
else:
    #print('Not available') # it's casesnsitive, hence answer is - Not Available
    None

# IF NOT
if a not in txt:
    #print('Not available')
    None
else:
    #print('Yes, present')
    None

# ====================================================================================

# Slicing
# defines Starting Index : End of Index
# Slice: Start, End, Interval ===>>> Interval applies after printing the first index... End of Index -1
aa = 'Hello Ram'
#print(slice(aa[2:3]))

py_string = 'Python_is_scripting_lang'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3)
#print(py_string[slice_object])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 6, 2)
#print(py_string[slice_object])   # yhn = 'Python_is_scripting_lang'

# stop = 3
# contains 0, 1 and 2 indices
slice_object = slice(3)
#print(py_string[slice_object])  # Pyt

# start = 1, stop = 6, step = 2
# contains 1, 3 and 5 indices
slice_object = slice(1, 12) #ython => h__
print(py_string[slice_object]) #Ram: yois

# Method 2 of SLICE
print(py_string[2:3])

# If start or End NOT emntioned considered as either 0 or full string
print(py_string[1:]) #pyt


# NEGATIVE VALUES
# Negatives starts from end..
# below 3 statemets retuns same result: _lang
print(py_string[-5:24])
print(py_string[-5:])
print(py_string[-5:len(py_string)+1])

# NEGATIVE first value should be greater than second value
# in POSITIVE VICE VERSA
# Should be greater than second value when one is NEGATIVE and another is Positive
print(py_string[-5:-1])
print(py_string[-5:15]) #_ p
