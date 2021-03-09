import pandas as pd
import numpy as np

d = {
    "one": pd.Series([1.0, 2.0, 3.0], index=["a", "b", "c"]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0], index=["a", "bb", "cc", "dd"]),
}
df = pd.DataFrame(d)
#print(df)
'''
    one  two
a   1.0  1.0
b   2.0  NaN
bb  NaN  2.0
c   3.0  NaN
cc  NaN  3.0
dd  NaN  4.0
'''
d = {
    "one": pd.Series([1.0, 2.0, 3.0]),
    "two": pd.Series([1.0, 2.0, 3.0, 4.0])
}
d1 = pd.DataFrame(d)
#print(d1)
'''
   one  two
0  1.0  1.0
1  2.0  2.0
2  3.0  3.0
3  NaN  4.0
'''
###########################################################################
# NOTE: If all rows don't have same length, then use pd.Series, otherwise it triggeres error.
###########################################################################
data1 = [1,2,3]
data2 = [5,6,7,8]
ddict = {
    'data1':pd.Series(data1),
    'data2':pd.Series(data2)
}
dd = pd.DataFrame(data=ddict)
#print(dd)
'''
   data1  data2
0    1.0      5
1    2.0      6
2    3.0      7
3    NaN      8
'''
###########################################################################
# NOTE: DF is a 2DM array, Rows have got Index, called row index. Where as Column names are column Index.
# as like row Index, we must use column names as column index.
###########################################################################

data = np.zeros((2,1), dtype=[("A", "i4"), ("B", "f4"), ("C", "a10"), ("D",'i4')])
#print(data)
#[(0, 0., b'') (0, 0., b'')]
#data[:] = [[(1, 2.0, "Hello")], [(2, 3.0, "World")]]
#print(data)
data[:] = [[(1, 2.0, "Hello",100)], [(2, 3.0, "World",1)]]
print(data)

###########################################################################

data2 = [{"a": 1, "b": 2}, {"a": 5, "b": 10, "c": 20}]
dict_df = pd.DataFrame(data2)
print(dict_df)
