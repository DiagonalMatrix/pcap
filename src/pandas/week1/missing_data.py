import pandas as pd
from src.datasets import data
import numpy as np

pd.options.display.width=None
netflix = data.netflix()

############################# REMOVE NULL ROWS #####################################################

#netflix_cut = netflix.loc[0:9]
#netflix_cut.loc[0:4, 5:6] = None

# Take copy of datacut
netflix_cut = netflix.loc[0:10]
#add custom column
netflix_cut = netflix_cut.reindex(columns=list(netflix_cut.columns)+['custom_col'])
# Assign a value
netflix_cut.loc[:7, 'custom_col'] = 100
#drop null rows.
netflix_cut = netflix_cut.dropna(how='any')
#print(netflix_cut)

############################# Fill NULLs #####################################################
netflix_cut = netflix.loc[0:10]
netflix_cut = netflix_cut.reindex(columns=list(netflix_cut.columns)+['col1','col2'])
netflix_cut['col1'] = netflix_cut['col1'].fillna(0)
netflix_cut['col2'] = netflix_cut['col2'].fillna('BBBBBB')
#print(netflix_cut)

#netflix_cut = netflix.fillna('AAA')
#print(netflix_cut)

if netflix_cut['director'].dtypes == 'object':
   netflix_cut['director'] = netflix_cut['director'].fillna('AAAAAAAA')

print(netflix_cut)

