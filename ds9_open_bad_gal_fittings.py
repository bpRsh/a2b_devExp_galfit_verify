#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
# Update      : Jun 27, 2017 Tue
# 
# Note: Run rename_files.py before running this program.
#
# Imports
import os
import subprocess
import glob
import re
import natsort
from astropy.io.fits import getval
import numpy as np

# Variables for ds9 flags
NCOLS                 = 4
NROWS                 = 2
flgs                  = '-scale log -cmap a -tile grid ' +\
                        'layout %d %d'%(NCOLS, NROWS)    + ' ' +\
                        '-match colorbar -match scale -match scalelimits' + ' '
# Variables for input fitsfiles to open
fit                   = '/Users/poudel/Research/galfit_usage/' +\
                        'verify_2cmp_fitting/f814w_fitting'
devauc_one_comp       = '%s/devauc_one_comp/f814w_devauc_one_comp'%fit
res_one_comp_devauc   = '%s/residual_one_comp_devauc/f814w_res_one_comp_devauc'%fit
expdisk_one_comp      = '%s/expdisk_one_comp/f814w_expdisk_one_comp'%fit
res_one_comp_expdisk  = '%s/residual_one_comp_expdisk/f814w_res_one_comp_expdisk'%fit
devauc_two_comp       = '%s/devauc_two_comp/f814w_devauc_two_comp'%fit
expdisk_two_comp      = '%s/expdisk_two_comp/f814w_expdisk_two_comp'%fit 
res_two_comp          = '%s/residual_two_comp/f814w_res_two_comp'%fit
gal                   = '%s/stamps_f8/f814w_gal'%fit



# These are obtained from summary_bad_fittings.py
visually_bad_gals = [9, 11, 12, 34, 35, 42, 88, 93, 99, 108, 111, 119, 126, 
                     134, 135, 136, 140, 144, 146, 147, 148, 149, 151, 152, 
                     156, 157, 162, 167, 169, 174, 179, 182, 184, 186, 189, 
                     194, 195, 196, 201, 204, 207, 208, 209, 211, 213, 214, 
                     215, 216, 217, 222, 224, 227, 231, 238, 249, 262, 264, 
                     267, 268, 269, 271, 276, 277, 284, 285, 287, 290, 298, 
                     299, 301] 
logfile_bad_gals  = [0, 7, 11, 12, 13, 27, 34, 35, 42, 43, 57, 61, 65, 66, 68, 
                    88, 93, 112, 113, 119, 126, 128, 144, 149, 155, 162, 167, 
                    189, 194, 195, 208, 211, 221, 227, 238, 246, 247, 250, 253, 
                    262, 264, 268, 269, 276, 284, 296, 297]
all_bad_gals    =  [0, 7, 9, 11, 12, 13, 27, 34, 35, 42, 43, 57, 61, 65, 66, 
                    68, 88, 93, 99, 108, 111, 112, 113, 119, 126, 128, 134, 
                    135, 136, 140, 144, 146, 147, 148, 149, 151, 152, 155, 156, 
                    157, 162, 167, 169, 174, 179, 182, 184, 186, 189, 194, 195, 
                    196, 201, 204, 207, 208, 209, 211, 213, 214, 215, 216, 217, 
                    221, 222, 224, 227, 231, 238, 246, 247, 249, 250, 253, 262, 
                    264, 267, 268, 269, 271, 276, 277, 284, 285, 287, 290, 296, 
                    297, 298, 299, 301] 

extra_visually_bad_gals =  [9, 99, 108, 111, 134, 135, 136, 140, 146, 147, 148, 
                            151, 152, 156, 157, 169, 174, 179, 182, 184, 186, 
                            196, 201, 204, 207, 209, 213, 214, 215, 216, 217, 
                            222, 224, 231, 249, 267, 271, 277, 285, 287, 290, 
                            298, 299, 301]
                            
                            
#nums = natsort.natsorted([int(re.search('(.+?)(\d+)(\.\w*)', f).group(2))
                              #for f in glob.glob(pth)])


all_bad_gals    =  [ 99, 108, 111, 112, 113, 119, 126, 128, 134, 
                    135, 136, 140, 144, 146, 147, 148, 149, 151, 152, 155, 156, 
                    157, 162, 167, 169, 174, 179, 182, 184, 186, 189, 194, 195, 
                    196, 201, 204, 207, 208, 209, 211, 213, 214, 215, 216, 217, 
                    221, 222, 224, 227, 231, 238, 246, 247, 249, 250, 253, 262, 
                    264, 267, 268, 269, 271, 276, 277, 284, 285, 287, 290, 296, 
                    297, 298, 299, 301] 
                              
nums = all_bad_gals

def open_in_ds9(nums):
    """Open fitsfiles in ds9 with some flgs.
    
    ds9 flgs:
        ds9 -scale log -cmap a -tile grid layout 4 2 -match colorbar
            -match scale -match scalelimits FITSFILES_NAMES

    Reference:
        http://ds9.si.edu/doc/ref/command.html#scale

    """

    files = [devauc_one_comp, res_one_comp_devauc,  res_one_comp_expdisk, expdisk_one_comp, 
             devauc_two_comp, res_two_comp,         expdisk_two_comp,     gal ]
    
    for n in nums:
        files_lst = [ (f + str(n) + '.fits ' + flgs) for f in files  ]
        files_all = " ".join(files_lst)
        
        # ds9 command with flags
        ds9 = '/Applications/ds9.app/Contents/MacOS/ds9' + ' '
        cmd = ds9 + ' -height 1200 ' + ' -width 2500 ' + files_all
        subprocess.call(cmd, shell=True)



if __name__ == "__main__":
    open_in_ds9(nums)
