#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jun 21, 2017 Wed
# Imports
import numpy as np
import pandas as pd
from pandas import DataFrame as DF

# Pandas setting to display long dataframe in terminal.
pd.set_option('display.width', None)
pd.set_option('precision', 3)
NCOLS = 7

# Break the data (Note that 43*7 = 301)
lst1, lst2 = np.arange(301), 0.333 * np.arange(301) # One row with 301 elements
arr1, arr2 = np.array_split(lst1, NCOLS), np.array_split(lst2, NCOLS) # 43*7 matrix

# Make dataframe
df1, df2 = DF(arr1).T, DF(arr2).T
columns = [ 'Galaxy_%d'%i for i in range(7)]
df1.columns, df2.columns = columns, columns

# Combine respective columns and create new df.
for i in range(7):
    df1.insert(i*2+1,'Diff_%d'%i,df2['Galaxy_%d'%i])

# Multi index from arrays
arr_idx = [ ['Group', '']*7, [ 'Galaxy', 'Diff' ]*7 ] # Double line top index
index   = pd.MultiIndex.from_arrays(arr_idx, names=['', '']) # leftmost index
df1.columns=index
print(df1)

# Write df1 into a file
df1.to_csv('tmp.txt',float_format='%.3f',sep='\t')
