########################################################################################################
# The open() function takes two parameters; filename, and mode.
# "r" - Read/"a" - Append/"w" - Write/"x" - Create
# you can specify handling mode - "t" - Text/"b" - Binary
########################################################################################################

#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists

import pandas as pd
from pandasql import sqldf

PATH = '/home/srujan/Documents/github/pcap/src/data/emp_data.txt'
readFile = open(PATH,'rt').read()

print('------- Input File in txt format-----------')
print(readFile)

def read_file(readfile):
    empId = []
    Basic_Pay = []
    incentives = []
    for line in readFile.split('\n'):
        lineIndex = line.split(',')
        empId.append(lineIndex[0])
        Basic_Pay.append(lineIndex[1])
        incentives.append(lineIndex[2])
    return empId, Basic_Pay, incentives

def list_dict(file_in_list):
    emp_id = {f'{file_in_list[0][0]}':file_in_list[0][1:]}
    Basic_pay = {f'{file_in_list[1][0]}':file_in_list[1][1:]}
    incentives = {f'{file_in_list[2][0]}':file_in_list[2][1:]}

    return emp_id, Basic_pay, incentives

def dict_df(dictionaries):
    emp_dict = {}

    for a in dictionaries:
        emp_dict.update(a)

    emp_data = pd.DataFrame(emp_dict)

    query = ''' SELECT * FROM emp_data WHERE Basic_pay > 12000 '''
    res = sqldf(query)
    print('------------ output file in DataFrame------------')
    print(res)

#====== CALLING fUNCTIONS ============
file_in_list = read_file(readFile)
dictionaries = list_dict(file_in_list)
dict_df(dictionaries)
