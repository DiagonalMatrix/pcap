x = 10
y = 'Srujan'

if type(x) == type(y):
    print('matched')
else:
    print('not maytched')

CONFPTH = '/home/srujan/Documents/API'


def retFruits():
    ap = 'Apple'
    ban = 'Banana'
    gr = 'Grape'

    return ap, ban, gr

# calling above function & returns TUPLE
fruits = retFruits()
#print(fruits)

# Assign Many Values to Multiple Variables

# EXAMPLE 1
apple, banana,grape  = fruits[0], fruits[1], fruits[2]
#print(apple, banana, grape)
#print(apple)
#print(banana)
#rint(grape)

#EXAMPLE 2
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

# Output Variables
a = 100
b = 201
empId = int(str(a)+str(b))
#print(type(empId))
#print(empId)


def empJoinYear():
    global dept
    dept = "IT"

empJoinYear()
#print(dept)

lst = [1,2,3,'Srujan']
tpl = (1,2,3,"srujan")
dit = {100:1,'b':2}

#print(lst)
#print(tpl)
#print(dit[100], dit['b'])

stt1 = (1,2,3,3,4,5,6,6,7,80,"srujan")
stt = set(stt1)
#print(stt)

s1 = {1,2,3,3,'srujan'}
#print('S1 is ====>',type(s1))
s2 = set(s1)
#print('s2 ====> ', type(s2))

s3 = [1,2,3,3,'srujan']
#print('s3 is list ===>', type(s3))
s4 = set(s3)
#print('s4 is set ==>>>', type(s4))

s5 = list(s4)
#print('s5 is a LIST ====>>> ', type(s5))

seet = set({1,2,3,4})
print(seet)
seet.add(5)
print(seet)

fz_set = frozenset({1,2,3,4})
print(fz_set)
fz_set

