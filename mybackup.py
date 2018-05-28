#!/usr/bin/python
# -*- coding: euc-kr -*-


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

###########
# imports #
###########
import os
import re
import sys
import time


###########
# options #
###########
reload(sys)
sys.setdefaultencoding("utf-8")


if __name__ == '__main__':

    source_dir = ['/Users/youngphilkwon/PycharmProjects']
    target_dir = '/Users/youngphilkwon/backup'

    backup_today_dir = target_dir + os.sep + time.strftime('%Y%m%d')
    today = time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')

    # target_zip_filename = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
    target_zip_filename = backup_today_dir + os.sep + now + '.zip'

    # check target dir and create target dir
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    if not os.path.exists(backup_today_dir):
        os.mkdir(backup_today_dir)

    # We use the zip command to put the files in a zip archive
    zip_command = "zip -r {0} {1}".format(target_zip_filename, ' '.join(source_dir))

    # Run the backup
    print "Zip command is:"
    print zip_command
    print "Running:"
    if os.system(zip_command) == 0:
        print 'Successful backup to', target_dir
    else:
        print 'Backup Failed'
