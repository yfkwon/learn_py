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
import sys
import time

# ===========================================================
# Program main routine
if __name__ == "__main__":
    f = None
    try:
        f = open("poem.txt")
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print line,
            sys.stdout.flush()
            print "Press ctrl+c now"
            # To make sure it runs for a while
            time.sleep(2)
    except IOError:
        print "Could not find file poem.txt"
    except KeyboardInterrupt:
        print "!! You cancellled the reading from the file."
    finally:
        if f:
            f.close()
        print "(Cleaning up: Closed the file)"

