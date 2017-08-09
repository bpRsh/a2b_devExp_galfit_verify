#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Jan 4, 2017
# Update      : Jun 22, 2017 Thu


# Imports
import os
import subprocess
import glob
import re
import natsort
from astropy.io.fits import getval
import numpy as np

# Variables
NCOLS                 = 5
NROWS                 = 4
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

                           
nums = [1, 14, 31, 33, 38, 40, 41, 44, 46, 52, 54, 56, 59, 69, 73, 
                76, 79, 80, 81, 85, 90, 92, 95, 138, 139, 141, 166, 180, 181, 
                200, 203, 218, 230, 243, 265, 266, 278, 293]

def open_in_ds9(nums):
    """Open fitsfiles in ds9 with some flgs.
    
    ds9 flgs:
        ds9 -scale log -cmap a -tile grid layout 6 4 -match colorbar
            -match scale -match scalelimits FITSFILES_NAMES

    Reference:
        http://ds9.si.edu/doc/ref/command.html#scale

    """

    files     = [devauc_one_comp, res_one_comp_devauc,  res_one_comp_expdisk, expdisk_one_comp, gal ]
    chunks = [nums[i:i + NROWS] for i in range(0, len(nums), NROWS)]
    for chunk in chunks:
        files_lst = [ (f + str(_) + '.fits ' + flgs)  for _ in chunk for f in files]
        files_all = " ".join(files_lst)
        
        # ds9 command with flags
        ds9 = '/Applications/ds9.app/Contents/MacOS/ds9' + ' '
        cmd = ds9 + ' -height 1200 ' + ' -width 2500 ' + files_all
        subprocess.call(cmd, shell=True)



if __name__ == "__main__":
    open_in_ds9(nums)
