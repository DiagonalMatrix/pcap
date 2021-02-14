#################################################
# The following script is used for SQL connection
# DT: 12/Feb/2021
# Author: Srujan
#################################################

# Mathematical operations
col1 = 100
col2 = 200
col3 = col1 + col2 # +, -, * /
#print(col3)



# variable scoping
class MyClass():

    var1 = '1000'

    def func1():
        myVar = 2000
        myVar2 = 300
        print(var1)

    func1()
    print(myVar)

