import pandas as pd

#1维列表
s = pd.Series([2,4,6,8],index=['a','b','c','d'])

#2维列表
d = pd.DataFrame([[2,4,6,8],[12,14,16,18]])

#索引创建Series
s1 = pd.Series({'a':1,'b':2,'c':3})

#可迭代对象创建
s2 = pd.Series(range(10))

#标量创建
s3 = pd.Series(10,index=[1,2,3])

print(s3)
