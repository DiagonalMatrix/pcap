import pandas as pd
from src.datasets import data
import numpy as np

pd.options.display.width=None
netflix = data.netflix()

######################### CONCATINATION #####################################

netflix_cut = netflix.iloc[:9, [0,1,6,7,8,9]]
#print(netflix_cut)
#print('---------------------------------------------')
pieces = [netflix_cut[:3], netflix_cut[2:6], netflix_cut[5:8], netflix_cut[7:8]]
netflix_conc = pd.concat(pieces)
#print(netflix_conc)

################### JOIN ###################################################

left = pd.DataFrame({'emp_id':[1,2,3,4,5,6], 'salary':[10000,20000,30000,40000,50000,60000]})
right = pd.DataFrame({'emp_id':[3,4,5], 'salary':[20000,30000,40000]})

lockdown_increments = pd.merge(left, right, how='left',on='emp_id')
#print(lockdown_increments)
#print('---------------------------')
lockdown_increments = pd.merge(left, right, how='right',on='emp_id')
#print(lockdown_increments)

################### GROUPING ###################################################

#print(netflix)
netflix_grpBy = netflix[netflix['release_year'] == 1945] #.groupby('release_year')
#print(netflix_grpBy)
netflix_rating = netflix_grpBy.groupby('rating').count()
#print(netflix_rating)
#print('-----------------')
netflix_mx = netflix_grpBy.max(axis=0)
#print(netflix_mx)
#print('----------------')
################### RESHAPING ###################################################
netflix_t = netflix.T
#print(netflix_t)

netflix['duration_mins'] = pd.to_numeric(netflix['duration'].apply(lambda row: row.split()[0]))
netflix_grpBy_pivot = pd.pivot_table(netflix, values=['duration_mins'], index=['release_year','type'], columns=['rating'])
#print(netflix_grpBy_pivot)
'''
                     duration_mins                                                                                                                             
rating                           G NC-17  NR         PG       PG-13          R       TV-14       TV-G      TV-MA       TV-PG       TV-Y      TV-Y7 TV-Y7-FV  UR
release_year type                                                                                                                                              
1925         TV Show           NaN   NaN NaN        NaN         NaN        NaN    1.000000        NaN        NaN         NaN        NaN        NaN      NaN NaN
1942         Movie             NaN   NaN NaN        NaN         NaN        NaN   35.000000        NaN        NaN         NaN        NaN        NaN      NaN NaN
1943         Movie             NaN   NaN NaN        NaN         NaN        NaN         NaN        NaN        NaN   62.666667        NaN        NaN      NaN NaN
1944         Movie             NaN   NaN NaN        NaN         NaN        NaN   58.000000        NaN        NaN   40.000000        NaN        NaN      NaN NaN
1945         Movie             NaN   NaN NaN        NaN         NaN        NaN   47.500000        NaN  59.000000         NaN        NaN        NaN      NaN NaN
...                            ...   ...  ..        ...         ...        ...         ...        ...        ...         ...        ...        ...      ...  ..
2019         TV Show           NaN   NaN NaN        NaN         NaN        NaN    1.979167   1.666667   1.754386    1.594595   1.772727   3.000000      NaN NaN
2020         Movie            48.0   NaN NaN  90.571429  101.157895  107.95122  103.622951  85.650000  93.502924   76.857143  38.500000  83.714286      NaN NaN
             TV Show           NaN   NaN NaN        NaN         NaN        NaN    1.887640   1.631579   1.671875    1.657143   1.878788   2.120000      NaN NaN
2021         Movie             NaN   NaN NaN        NaN         NaN  116.00000   33.333333        NaN  93.166667  102.000000        NaN  85.000000      NaN NaN
             TV Show           NaN   NaN NaN        NaN         NaN        NaN    2.250000   1.500000   1.625000    3.000000   1.000000   3.000000      NaN NaN
'''


netflix_grpBy = netflix[netflix['release_year'] == 1984]
netflix_size = netflix_grpBy.groupby('rating').size()
netflix_cast = netflix_grpBy.groupby('cast').size()
#print(netflix_cast)
'''
rating
TV-14    2
TV-MA    1
dtype: int64
'''
netflix_cnt = netflix_grpBy.groupby('release_year').count()
netflix_cnt = netflix_grpBy.groupby('rating').count()
#print(netflix_cnt)
'''
        show_id  type  title  director  cast  country  date_added  release_year  duration  listed_in  description  duration_mins
rating                                                                                                                          
TV-14         2     2      2         2     1        2           2             2         2          2            2              2
TV-MA         1     1      1         1     0        1           1             1         1          1            1              1
'''
#print(netflix[netflix['release_year'] == 1945])


################## Categoricals ##################################################
# 'TV-MA' = 'TV Mature Audience'
# 'R' = 'Restricted'
# 'PG-13' = 'Over 13'
# 'TV-14' = 'Over 13'
# 'TV-PG' = 'Parental Guidance'
# 'NR' = 'Unrated'
# 'TV-G' = 'Over 14'
# 'TV-Y' = 'ages 2 to 6'
# nan
# 'TV-Y7' = 'Over 7'
# 'PG' = 'Over 8'
# 'G' = 'General Audiences'
# 'NC-17' = 'Over 17'
# 'UR' = 'Unrated'

netflix_cat = netflix['rating'].astype('category')
print(netflix_cat)
'''
Name: rating, Length: 7787, dtype: category
Categories (14, object): ['G', 'NC-17', 'NR', 'PG', ..., 'TV-Y', 'TV-Y7', 'TV-Y7-FV', 'UR']
'''

#netflix_cat['rating'].cat.categories = []














