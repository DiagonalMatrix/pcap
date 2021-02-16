py_string = ' Python, is, scripting, lang '

print(py_string.upper())
print(py_string.lower())


#====== REMOVE SPACES =============
# REMOVES prefix & Suffix of a string
print(py_string.strip())

#============ REPLACE =============
print(py_string.replace('is','are'))
print(py_string.split(','))

# =========== SPLIT ==============
txt_doc = 'Hello my name is srujan'
print(txt_doc.split(' '))

# =========== CONCATINATION ========
# NOTE: if both are strings then concatinates, if both are int then SUMS
# It must be both STRINGS or BOTH INT

age = 36
txt = "My name is John, I am " + str(age) # ERROR if str() not Used.
#print(txt)

age = 36
txt = 40
#print(age+txt)

# =========== format ============
#METHOD 1
age = 36
txt = "My name is John, I am {}".format(age)
print('format METHOD 1 =====>>>',txt)

# Method 2:
age = 36
txt = f"My name is John, I am {age}"
print('format METHOD 2 =====>>>',txt)

# Method 3:
age = 36
work = 'consultant'
txt = "My name is John, I am {} and I work as {}".format(age, work)
print('format METHOD 3 =====>>>',txt)

# Method 4:
age = 36
work = 'consultant'
txt = "My name is John, I work as a {1} and my name is {0}".format(age,work)
print('format METHOD 4 =====>>>',txt)

port = 1234
uri = 'abcd.com'
api = 'mysql'
user = 'srujan'
pwd = 'myPass'
mySQL = api+'/'+uri+':'+user+':'+pwd+'/'+str(port)
mySQL1 = "{}:{}:{}:{}:{}".format(api,uri,user,pwd,port)
print('mySQL =====>>> ',mySQL)
print('mySQL1 =====>>> ',mySQL1)


# =============== ESCAPE ==============
# METHOD 1
txt = "We are the so-called \"Vikings\" from the north."
#Method 2
txt1 = 'We are the so-called "Vikings" from the north.'
print(txt1)
print(txt)
