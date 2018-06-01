#!/usr/bin/python
# -*- coding: euc-kr -*-

# ===========================================================
"""program information"""
__author__ = "young phil, kwon"
__date__ = "creation: 2018-06-01, modification: 2018-06-01"
__copyright__ = "Copyright 2018, The StartPy Project"
__credits__ = ["young phil kwon", "Star Play Lab"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "young phil kwon"
__email__ = "yfkwon@starplay.io"
__status__ = "Test Bed"


# ===========================================================
# Imports
import pickle

# ===========================================================
# Program main routine
if __name__ == "__main__":
    # The name of the file where we will store the object
    shoplist_file_name = 'shoplist.data'
    # The list of things to buy
    shoplist = ['apple', 'mango', 'carrot']

    # Write to the file
    f = open(shoplist_file_name, 'wb')
    # Dump the object to a file
    pickle.dump(shoplist, f)
    f.close()

    # Destory the shoplist variable
    del shoplist

    # Read back from the storage
    f = open(shoplist_file_name, 'rb')
    # Load the object from the file
    storedlist = pickle.load(f)
    print storedlist
