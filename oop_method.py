#!/usr/bin/python
# -*- coding: euc-kr -*-

# ===========================================================
"""program"""
__author__ = "young phil, kwon"
__date__ = "creation: 2018-05-24, modification: 2018-05-24"
__copyright__ = "Copyright 2018, The StartPy Project"
__credits__ = ["young phil kwon", "Star Play Lab"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "young phil kwon"
__email__ = "yfkwon@starplaylab.com"
__status__ = "Test Bed"
# ===========================================================

# ===========================================================
# imports
# ===========================================================

# ===========================================================

# Person class
class Person:
    """
    Person Class
    """
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print 'Hello, my name is', self.name

# Program Main Routine
if __name__ == '__main__':

    p = Person('Swaroop')
    p.say_hi()
    # The previous 2 lines can also be written as
    # Person('Swaroop').say_hi()
