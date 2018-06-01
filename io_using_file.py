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

# ===========================================================
# Imports
# ===========================================================
import os.path

# ===========================================================
# Define functions


# Program main routine
if __name__ == "__main__":
    poem = '''\
    Programming is fun
    When the work is done
    if you wanna make your work also fun:
        use Python!
    '''

    # Open for 'w'riting
    f = open('poem.txt', 'w')
    # Write text to file
    f.write(poem)
    # Close the file
    f.close()

    if os.path.isfile('./poem.txt') != True:
        print 'Poem.txt file not exist'
    else:
        print 'Poem.txt file is exist'

    # If no mode is specified,
    # 'r'ead mode is assumed by default
    f = open('poem.txt', 'r')
    while True:
        line = f.readline()
        # Zero length indicates EOF
        if len(line) == 0:
            break
        # The 'line' already has a newline
        # at the end of each line
        # since it is reading from a file.
        print line,
    # Close the file
    f.close()

