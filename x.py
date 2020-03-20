#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:13:20 2020

@author: lf
"""
import pandas as pd
import numpy as np

df = pd.read_csv('/home/lf/mysql_data/100.csv')

tmp = df.head(10)

tmp.loc[0]=np.nan

print(tmp.dropna(how='any'))

print(tmp['money'].mean())

x = df.to_csv('/lf')