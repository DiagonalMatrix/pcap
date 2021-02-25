########################################################################################################
# Try: Execute peace of code
# Exception: Either display error message as it is or convey it in a human readable format.
# finally: ??
########################################################################################################
#x = 'a'
#y = x/2

x = 1
y = '' #1/0

try:
    y
except BaseException as be:
    print(be, 'Please try integer')
except RuntimeError as re:
    print(re)
except TypeError as te:
    print(te)


########################################################################################################
# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:
# NameError, SyntaxError, TypeError etc.,
########################################################################################################

#a

try:
    print()#a
except NameError as ne:
    print(ne) #NameError: name 'a' is not defined

########### exception else ##########################################
#NOTE:
# Here after Try, default Except = True else False logic applies.

try:
    print ('a') #('')
except:
    print('There is an error')
else:
    print('No errors')

########### Try/except/Finally ##########################################
# NOTE: Unline else condition.. here Finally MUST executes irrespective of Success/Failure

try:
    print('Connect to DB')
except:
    print('Access DB failure')
finally:
    print('close DB connection.')

######### Raise Exeception ##############################################

# Example 1
a = 21
b = 20

if a < b:
    raise Exception('a MUST always be greater than b!')
# Exception: a MUST always be greater than b!

# Example 2
age = 'Hello'

if type(age) is not int:
    raise Exception('Age must always be an Integer! Pls Try again.')
# Exception: Age must always be an Integer! Pls Try again.
