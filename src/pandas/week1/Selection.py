####################################################################################
# Selection of Dataframe content
####################################################################################
import pandas as pd
from src.datasets import data
from tabulate import tabulate

pd.options.display.width=None
netflix = data.netflix()

#------------------ SELECT BY Columns --------------------------------------------
#NOTE: Keep all columns in list of list

# Show single column(s)
single = netflix[["show_id"]]
#print(single)

# Show multiple columns
multi = netflix[["show_id","type"]]
#print(multi)

#------------------ SELECT SLICE of ROWS --------------------------------------------
first_3Rec = netflix[0:3]
#print(first_3Rec)

################################ selection by Label ##################################
# loc: search based on 'row index'....
# List all columns..
#####################################################################################
single_row = netflix.loc[0]
#print(single_row)c

multi_row = netflix.loc[0:3]
#print(multi_row)

# Scenario:
# Display first column and first 5 records

#Method 1:
multi_row = netflix[['show_id']].loc[:4]
#print(multi_row)

#Scenario: Display 1st row of 1st column
first_first = netflix[['type']].loc[0]
#print(first_first)
first = netflix.loc[0,['type']]
#print(first)

#Method 2:
method2 = netflix.loc[3:8, ['show_id','type']]
#print(method2)

###############################################################
# Scenario, multiple columns by row index
col = list(netflix.columns)

#Method 1:
multi_1 = netflix.loc[:,['show_id', 'type']]

# Method 2:
multi_2 = netflix.loc[:, col[0:3]]
#print(multi_2)


######################### Use above scenarion with iloc ######################################
# iloc is nothing but Access by position
# syntax iloc[row_index, colmn_indx]

# Difference: iloc, access index-1, where as loc access index

first = netflix.iloc[0:7, 2:5]
#print(first)

method2 = netflix.loc[0:7, ['show_id','type']]
#print(method2)
##############################################################################################
