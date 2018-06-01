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
# imports
# ===========================================================

# ===========================================================
# define function

def reverse(text):
    """
    function reverse
    :param text:
    :return:
    """
    return text[::-1]

def is_palindrome(text):
    """
    function is_palindrome
    :param text:
    :return:
    """
    return text == reverse(text)

if __name__ == "__main__":
    something = raw_input("Enter text:")

    if is_palindrome(something):
        print "Yes, it is a palindrome"
    else:
        print "No, it is not a palindrome"

