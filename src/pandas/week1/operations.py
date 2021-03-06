import pandas as pd
from src.datasets import data
import numpy as np
from datetime import date

pd.options.display.width=None
netflix = data.netflix()

########################### iloc vs loc ##########################################
#Note: iloc got too flexibility, you can give rows or columns or both
# but for loc only rows are allowed.

netflix_cut = netflix.iloc[0:9, 0:5]
#print(netflix_cut)

netflix_cut = netflix.iloc[0:9, [1,3,5]]
#print(netflix_cut)

netflix_cut = netflix.iloc[[1,3,4], [1,3,5]]
#print(netflix_cut)

netflix_cut = netflix.loc[[1,3,6]]
#print(netflix_cut)

# without loc/iloc
netflix_cut = netflix[:9]
#print(netflix_cut)

########################### Apply ##########################################
netflix_cut = netflix.iloc[:9, [1,6,7,8,9]]
tday = date.today().year
netflix_cut['years_old'] = netflix_cut['release_year'].apply(lambda row: tday-row)
#print(netflix_cut)

#======================= apply max-min on entire column, not rows ============
netflix_years = netflix_cut.iloc[:4, [2,5]]
#print(netflix_years)
netflix_years = netflix_years.apply(lambda row: row.max() - row.min())
#print(netflix_years)

