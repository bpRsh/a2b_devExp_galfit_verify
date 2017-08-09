#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jun 10, 2017 Sat
# Last update : 
#
# Imports
# write to a file
# Imports
import numpy as np
import pandas as pd
from pandas import DataFrame as DF

## Break the data
all_bad_gals    =  [0, 7, 9, 11, 12, 13, 27, 34, 35, 42, 43, 57, 61, 65, 66, 
                    68, 88, 93, 99, 108, 111, 112, 113, 119, 126, 128, 134, 
                    135, 136, 140, 144, 146, 147, 148, 149, 151, 152, 155, 156, 
                    157, 162, 167, 169, 174, 179, 182, 184, 186, 189, 194, 195, 
                    196, 201, 204, 207, 208, 209, 211, 213, 214, 215, 216, 217, 
                    221, 222, 224, 227, 231, 238, 246, 247, 249, 250, 253, 262, 
                    264, 267, 268, 269, 271, 276, 277, 284, 285, 287, 290, 296, 
                    297, 298, 299, 301] 
                    
arr1 = np.array_split(all_bad_gals, 7)
df1 = DF(arr1).T
df1.to_csv('tmp.txt',sep='\t',index=None,header=None,float_format='%d')

