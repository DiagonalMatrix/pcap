##########################################################################################
# Pandas Series is a one-dimensional labeled array capable of holding data of any type (integer, string, float, python objects, etc.).
# The axis labels are collectively called index. Pandas Series is nothing but a column in an excel sheet.
##########################################################################################
import pandas as pd
import numpy as np

data = [1,2,3,'ram','ramesh',10,12]
df = pd.DataFrame(data,columns=['names'])
#print(df)

# Series
data = pd.Series([1,2,3,'ram','ramesh',10,12])
#print(data)


#Date Range#
dates1 = pd.date_range(start='2021-01-01',end='2021-12-31',freq='D')
dates2 = pd.date_range('2021-01-01',periods=12,freq='M')
dates3 = pd.date_range('2021/01/01',periods=12,freq='M')
#print(dates1)

#Dataframe
df = pd.DataFrame(np.random.randn(365,4), index=dates1, columns=['col1','col2','col3','col4'])
#print(df)


# datfraem
df2 = pd.DataFrame({
         "A": 1.0,
         "B": pd.Timestamp("20130102"),
         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
         "D": np.array([3] * 4, dtype="int32"),
         "E": pd.Categorical(["test", "train", "test", "train"]),
         "F": "foo",})

# NOTE: DataFrame requires at least one iterable object for indexing.
# otherwise put dict in a list for indxing.
df3 = pd.DataFrame(
    [{
        'a': 'aa',
        'B': 'c',
        'c': 1
    }]
)
dtyp = df3.dtypes
print('Data types of a df ====> ',dtyp)
print('Access dtypes ====> ',dtyp[0],dtyp[1],dtyp[2])

if dtyp[2] == 'int64':
    print('correct')

# Defualt records..
print(df) # list displys top 5 & bottom 5 records
print(df.head()) # displays first 5 records
print(df.tail()) # displays last 5 records
id = df.index
print('The id\'s are: ',id)


#print(df.columns)

# Turn columns_to_rows, Transposing your data
print(df.T)
'''
      2021-01-01  2021-01-02  2021-01-03  ...  2021-12-29  2021-12-30  2021-12-31
col1   -0.689319    0.278504    0.082439  ...    0.594000   -0.555328   -0.709003
col2   -0.732336    0.285436    0.833684  ...   -0.432952    2.245070    1.416092
col3   -2.005206    1.104812    0.457625  ...    0.445861   -2.767915   -1.075880
col4    0.872063    0.584907    0.913729  ...    1.575664    0.883240   -0.281696
'''


# df.describe()
#print(df.describe())
'''
             col1        col2        col3        col4
count  365.000000  365.000000  365.000000  365.000000
mean    -0.004925   -0.127556    0.010276   -0.044688
std      1.017037    0.992857    1.030455    1.052531
min     -3.342717   -3.073764   -3.476341   -3.265240
25%     -0.766998   -0.859692   -0.646700   -0.766662
50%     -0.041268   -0.119884   -0.003172   -0.106301
75%      0.703978    0.569841    0.707047    0.689715
max      2.856209    3.071998    2.768758    3.352297
'''

