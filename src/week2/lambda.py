###################################################################
# Lambda, annonimus function, accepts N number of aruguments.
# A function which has got no name
# single line function.
###################################################################

import pandas as pd

#simple lambda function
col3 = lambda col1, col2: (col1 + col2) * 2
print(col3(100,200)) # 600

# Apply lambda in a function
def read_table(path,output):
    emp_data = pd.read_csv(path, index_col=False)
    emp_data['total_salary'] = emp_data.apply(lambda row: (row['Basic_pay'] + row['incentives']), axis=1)
    emp_data.to_csv(f'{output}emp_processed.csv',index=False)


inputPath = '/home/srujan/Desktop/emp_data.csv'
output = '/home/srujan/Desktop/'
res = read_table(inputPath,output)



