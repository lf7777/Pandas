import pandas as pd

#1维列表
s = pd.Series([2,4,6,8,4],index=['a','b','c','d','e'])

#2维列表
d = pd.DataFrame([[2,4,6,8],[12,14,16,18]],index=['a','b'],columns=['a','b','c','d'])

#索引创建Series
s1 = pd.Series({'a':1,'b':2,'c':3})

#可迭代对象创建
s2 = pd.Series(range(10))

#标量创建
s3 = pd.Series(10,index=[1,2,3])

s[['a','b']]=44

s.index = [3,4,5,6,7]

print(d.iloc[0])
