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


# ===========================================================
# Program main routine
if __name__ == "__main__":
    try:
        text = raw_input('Enter something --> ')
    except EOFErro:
        print 'Why did you do an EOF on me?'
    except KeyboardInterrupt:
        print 'You cancelled the operation.'
    else:
        print 'You entered {}'.format(text)
