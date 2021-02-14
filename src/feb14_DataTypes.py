# data Types
import random
'''
for a in range(10):
    print(a)
'''
a = random.randrange(10,15)
#print('Rand ramnge is ',a)


f = 100.5623
#print(type(f))
ff = int(f)
#print(ff)
#print(type(ff))

# Multiline string
multi_line_string = '''
Hello friends
this is python certification
training.
'''
#print(multi_line_string)

multi_lines_in_string = 'hello friends ' \
                        'this is PCAP ' \
                        'session'
#print(multi_lines_in_string)

#for a in [1,2,3,4,5,6,7,8,9,10]:
    #print(a)
 #   None

lst = [2,2,3,3,4,5,6,7,8,9,10]

for a in range(len(lst)):
    #print(lst[a])
    None

i = 0
while i <= 10:
    #print(i)
    i+=1
emp_id = [100,200,300,400]
emp = 400
if emp in emp_id:
    #print(True)
    None


emp_tf = emp not in emp_id
print(emp_tf)
