####################################################################################
# Functions
# *args is called Arbitary Argument, pass arguments in TUPLE
# **kwargs is called Arbitary Keyword Arguments, pass arguments in DICTIONARY
# you can use any name *name **names
####################################################################################

def myFirstFunction():
    pass

def MySecondFunction(*args):
    #arguments in a Tuple access with Index
    print(args[1])
MySecondFunction(123,'srujan')

def my_third_funtion(**kwargs):
    # arguments returns in a Key/Value pair
    for a,b in kwargs.items():
        print(f'key is: {a} and value is: {b}')

my_third_funtion(name='srujan',loc='reading')


print('============ USE ANY ARG NAME ===========')


def funtionNameChange(*name):
    print('====>>>> funtionNameChange')

funtionNameChange('srujan', 123)

def FunctionArgs(**names):
    print('====>>>> FunctionArgs')
FunctionArgs(name='Srujan', loc='Reading')


# ====================== DEFAULT ARGUMENTS ===========================
print('# ====================== DEFAULT ARGUMENTS ===========================')

def def_args(country = 'UK'):
    print(country)

def_args('Norway')
def_args()
