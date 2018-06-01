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
import io

# ===========================================================
# Program main routine
if __name__ == "__main__":
    utf_file_name = "euck_file.txt"

    f = io.open(utf_file_name, 'wt', encoding='utf-8')
    f.write(u"Imagine non-English language here, 한글로 쓰기")
    f.close()

    utf_text_file = io.open(utf_file_name, encoding='utf-8')

    while True:
        utf_text_line = utf_text_file.readline()

        if len(utf_text_line) == 0:
            break

        print utf_text_line

