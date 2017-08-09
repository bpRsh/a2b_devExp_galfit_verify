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
NCOLS = 6
NROWS = 4
galfit_outputs       = 'f814w_fitting'          
pth                  = '/Users/poudel/Research/galfit_usage/verify_2cmp_fitting/' +\
                       '%s/devauc_two_comp/f814w_devauc*.fits'%(galfit_outputs)
gal                  = '/Users/poudel/jedisim/z_jedisim_dev_sim/galaxies/f814w_gal'
fit                  = '/Users/poudel/Research/galfit_usage/verify_2cmp_fitting/' + galfit_outputs 
devauc_two_comp      = '%s/devauc_two_comp/f814w_devauc_two_comp'%fit
expdisk_res_two_comp = '%s/expdisk_res_two_comp/f814w_expdisk_res_two_comp'%fit 
residual_two_comp    = '%s/residual_two_comp/f814w_res_two_comp'%fit
devauc_one_comp      = '%s/devauc_one_comp/f814w_devauc_one_comp'%fit 
expdisk_res_one_comp = '%s/expdisk_res_one_comp/f814w_expdisk_res_one_comp'%fit
flgs                 =  '-scale log -cmap a -tile grid layout %d 4'%NCOLS + ' ' +\
                        '-match colorbar -match scale -match scalelimits' + ' '

                           
nums = natsort.natsorted([int(re.search('(.+?)(\d+)(\.\w*)', f).group(2))
                              for f in glob.glob(pth)])

def open_in_ds9(nums):
    """Open fitsfiles in ds9 with some flgs.
    
    ds9 flgs:
        ds9 -scale log -cmap a -tile grid layout 6 4 -match colorbar
            -match scale -match scalelimits FITSFILES_NAMES

    Reference:
        http://ds9.si.edu/doc/ref/command.html#scale

    """

    files     = [ devauc_two_comp, expdisk_res_two_comp, residual_two_comp, 
                  devauc_one_comp, expdisk_res_one_comp, gal ]
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
