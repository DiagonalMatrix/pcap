
PATH = '/home/srujan/Documents/github/pcap/src/data/emp_data.txt'
FILE_PATH = '/home/srujan/Desktop/emp.txt'
import datetime

read_file = open(PATH,'r')

# read whole file
#whole_file = read_file.read()
#print(whole_file)

# single line
'''
print(read_file.readline())
print(read_file.readline())
print(read_file.readline())
read_file.close() '''

#################################################################################
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
##################################################################################
write_text = '\nSample Test Data'

# APPEND Scenario
appendFile = open(FILE_PATH,'at')
appendFile.write(write_text)
appendFile.close()

read = open(FILE_PATH,'r')
#print(read.read())

# Write Scenario
def looping():
    txt = ''
    for _ in range(10):
        dt = datetime.datetime.now()
        txt += str('\nSample Test Data - '+str(dt))
    return txt

FILE_PATH = '/home/srujan/Desktop/TransLog.txt'
write_file = open(FILE_PATH,'w') #Default text is format.
write_file.write(looping())
write_file.close()

file = open(FILE_PATH,'r').read()
#print(file)

#################################################################################
# "x" - Create - will create a file, returns an error if the file exist
##################################################################################

tstamp = datetime.datetime.now()

#Scenario Create: Create a log file.
FILE_PATH = f'/home/srujan/Desktop/logs/{tstamp}.txt'
def looping():
    txt = ''
    for _ in range(10):
        dt = datetime.datetime.now()
        txt += str('\nSample Test Data - '+str(dt))
    return txt

logFile = open(FILE_PATH,'x')
logFile.write(looping())
logFile.close()

readLog = open(FILE_PATH,'r')
print(readLog.read())

