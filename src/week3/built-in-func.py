###########################################################################
# The compile() function returns the specified source as a code object, ready to be executed.
#
###########################################################################

#Syntax
#compile(source, filename, mode, flag, dont_inherit, optimize)

def myFunc(a):
    for a in range(a):
        pass
        #print(a)

call = myFunc(10)
res = compile('call','myFunc','eval')
exec(res)

###################### delattr, removes object ###########################################

class Person:
    name = 'John'
    age = 36
    country = 'Norway'

delattr(Person,'age')

p = Person
#print(p)

###################### delattr, removes object ###########################################

x = dict(name = "John", age = 36, country = "Norway")
#print(x)


############### dir() ####################################################################
# This function will return all the properties and methods, even built-in properties which are default for all object.
############### dir() ####################################################################

class student:

    name = 'srujan'
    id = 100
    loc = 'Reading'

res = dir(student)
#sprint(res)

########## divmod() method ##################################################################
# returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).
x = divmod(5,1)
#print(x)

######### enumerate() #######################################################################
# Takes collection, assign index value to each element, and returns tuple
# enumerate(iterable, start)

col = ('apple', 'banana', 'cherry')
y = enumerate(col)
#print(list(y))
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

col1 = ['apple', 'banana', 'cherry']
yy = enumerate(col1)
#print(list(yy))

################### eval() & expr() ###############################################################

res = eval('(10+10)/2')
print(res)
print(eval ('"srujan " + "kumar"'))

##### exec()
x = """
a = 10+10\n
b = a*2\n
c = a+b\n
print(c)
"""
exec(x)

# diff between eval & exec,
# eval evaluates single line string to python code and exec multi line code.

############### filter ######################
# filter takes 2 args: function and arguments
# returns True elements only from args.

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
      if x < 18:
        return False
      else:
        return True

adults = filter(myFunc,ages)

for age in adults:
    print(age)



################# floating ##########################

i = 12.23245
ii = 12.30000
print(float(i)) # 12.23245
print(float(ii)) # 12.3

################# formating ##########################

val = format('Hello Ramesh & Ram', '>')
print('Format ',val)
val = format('Hello Ramesh & Ram', '<')
print('Format ',val)
val = format(10000000, ',')
print('Format ',val) # Format  10,000,000

############# frozenset ###########################
# Set is mutable, where as frozenset is immutable
sets = {1,2,3,4}
sets = frozenset(sets)
print('FrozenSet ',type(sets))

############# getAttribute() #####################
class Person:
    '''
    This is a simple class
    '''
    name = 'Srujan'
    age = 21
    loc = 'Reading'

att = getattr(Person, 'age') #Attribute val must be in string.
print(att)

############### HELP ############################
print(help(Person))

x = globals()
print(x["__file__"])


i = 10
inst = isinstance(i, int)
print(inst)

########### map() ############################
# map returns a list
# Advanatge, for loop is not neccessary.
def comput(a):
    a = a*2
    if a > 2:
        return True
    else:
        return False

col=[2,1,3,4,1]
x = map(comput,col)
print('Map is ',list(x))

x= comput(2)
print(x)
###############################################
