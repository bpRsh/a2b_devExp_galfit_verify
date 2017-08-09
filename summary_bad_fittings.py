#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jun 22, 2017 Thu
# Last update : 
#
# Imports
import numpy as np

visually_bad_gals = [9, 11, 12, 34, 35, 42, 88, 93, 99, 108, 111, 119, 126, 
                     134, 135, 136, 140, 144, 146, 147, 148, 149, 151, 152, 
                     156, 157, 162, 167, 169, 174, 179, 182, 184, 186, 189, 
                     194, 195, 196, 201, 204, 207, 208, 209, 211, 213, 214, 
                     215, 216, 217, 222, 224, 227, 231, 238, 249, 262, 264, 
                     267, 268, 269, 271, 276, 277, 284, 285, 287, 290, 298, 
                     299, 301] 
logfile_bad_gals  = [0, 7, 11, 12, 13, 27, 34, 35, 42, 43, 57, 61, 65, 66, 68, 88, 
             93, 112, 113, 119, 126, 128, 144, 149, 155, 162, 167, 189, 194, 
             195, 208, 211, 221, 227, 238, 246, 247, 250, 253, 262, 264, 268, 
             269, 276, 284, 296, 297]

common_bad_gals = [x for x in visually_bad_gals if x in logfile_bad_gals]
all_bad_gals = list(set(  visually_bad_gals+logfile_bad_gals ))
extra_visually_bad_gals = [i for i in visually_bad_gals if i not in logfile_bad_gals]
symmetric_difference = list(set(visually_bad_gals).symmetric_difference(set(logfile_bad_gals)))
#extra_visually_bad_gals = list( set(visually_bad_gals) - set(logfile_bad_gals))

print('common_bad_gals = ', common_bad_gals,'\n')
print('all_bad_gals    = ', all_bad_gals,'\n')
print('extra_visually_bad_gals = ', extra_visually_bad_gals, '\n')
print('symmetric_difference = ', symmetric_difference,'\n')

print('len common_bad_gals = ', len(common_bad_gals))
print('len all_bad_gals    = ', len((all_bad_gals)))
print('len extra_visually_bad_gals = ', len(extra_visually_bad_gals), '\n')
