#!/usr/local/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics PhD Student, Ohio University
# Date        : May 10, 2017 Wed
# Last update : Jun 19, 2017 Mon
# Est time    :
#
# Imports
import os
import glob
import re
import time

# Rename filenames
def rename_files(idir,old,new):
    """ Rename all files in a folder.
    Arguments:
    Exmaples:
    idir = f814w_fitting/devauc_one_comp
    old  = f814w_devauc
    new  = f814w_devauc_one_comp
    
    """
    files = glob.glob(idir + '/' + old + '*.fits')
    for f in files:
        try:
            # f814w_fitting/devauc_one_comp/f814w_devauc0.fits
            f2 = f.replace(idir + '/' + old, idir + '/' + new)
            os.rename(f, f2)
            print("\n")
            print('From: ', f)
            print('To  : ', f2)
        except:
            pass

def main():
    # devauc_one_comp
    idir = 'f814w_fitting/devauc_one_comp'
    old  = 'f814w_devauc'
    new  = 'f814w_devauc_one_comp'
    rename_files(idir,old,new)
    
    # residual_one_comp_devauc
    idir = 'f814w_fitting/residual_one_comp_devauc'
    old  = 'f814w_res'
    new  = 'f814w_res_one_comp_devauc'
    rename_files(idir,old,new)
    
    # expdisk_one_comp
    idir = 'f814w_fitting/expdisk_one_comp'
    old  = 'f814w_expdisk'
    new  = 'f814w_expdisk_one_comp'
    rename_files(idir,old,new)
    
        
    # residual_one_comp_expdisk
    idir = 'f814w_fitting/residual_one_comp_expdisk'
    old  = 'f814w_res'
    new  = 'f814w_res_one_comp_expdisk'
    rename_files(idir,old,new)
    
    # devauc_two_comp
    idir = 'f814w_fitting/devauc_two_comp'
    old  = 'f814w_devauc'
    new  = 'f814w_devauc_two_comp'
    rename_files(idir,old,new)
    
    
    # expdisk_two_comp
    idir = 'f814w_fitting/expdisk_two_comp'
    old  = 'f814w_expdisk'
    new  = 'f814w_expdisk_two_comp'
    rename_files(idir,old,new)
    
    # residual_two_comp
    idir = 'f814w_fitting/residual_two_comp'
    old  = 'f814w_res'
    new  = 'f814w_res_two_comp'
    rename_files(idir,old,new)


##==============================================================================
## Main program
##==============================================================================
if __name__ == '__main__':
    # Beginning time
    begin_time,begin_ctime = time.time(), time.ctime()

    # Run main program
    main()

    # Print the time taken
    end_time,end_ctime  = time.time(), time.ctime()
    seconds             = end_time - begin_time
    m, s                = divmod(seconds, 60)
    h, m                = divmod(m, 60)
    d, h                = divmod(h, 24)
    print('\nBegin time: ', begin_ctime,'\nEnd   time: ', end_ctime,'\n' )
    print("Time taken: {0:.0f} days, {1:.0f} hours, \
          {2:.0f} minutes, {3:f} seconds.".format(d, h, m, s))

