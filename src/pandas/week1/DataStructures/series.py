##################################################################################################
# Series is a one-dimensional labeled array capable of holding any data type
# (integers, strings, floating point numbers, Python objects, etc.).
# NaN (not a number) is the standard missing data marker used in pandas.
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
#print(s)
'''
a    0.264394
b    2.454670
c    0.300453
d    0.016809
e    0.086761
dtype: float64
'''

s1 = s+s
#print(s1)
'''
a    0.528787
b    4.909340
c    0.600906
d    0.033618
e    0.173522
dtype: float64
'''

s2 = s[1:] + s[:-1]
print(s2)
'''
a         NaN
b    4.909340
c    0.600906
d    0.033618
e         NaN
dtype: float64
'''
s3 = s[:4]
print(s3)
'''
a    1.005105
b    1.170188
c   -0.480760
d    0.421191
'''
