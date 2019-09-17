# -*- coding: utf-8 -*-
# This program provides utility functions
# Author : Anwar Buchoo (luckyhuss@msn.com)
# Date : 16-Sep-2016
# Version : 1.0

import io
import os
import sys
import time
from contextlib import redirect_stdout

from dirsync import sync

import mylogger

# application paths
PATH_BASE = os.path.dirname(os.path.realpath(__file__))
PATH_LOG = os.path.normpath(PATH_BASE + "/logs")

# application files
FILE_LOG = os.path.normpath(PATH_LOG + "/main.log")

# application variables
purge = False

def error(e):
	mylogger.logger.error("Error {0}".format(e))
	
def debug(message):
	mylogger.logger.debug(message)

def info(message):
	mylogger.logger.info(message)
	
def warn(message):
	mylogger.logger.warning(message)

def startTimer():
	# get start time
	return time.time()
	
def stopTimer(startTimer):
	# set time taken to execute statement
	return str(round(time.time() - startTimer, 2))

def directorySync(key, PATH_SRC, PATH_DEST, backwardPass):
	"""Sync the folders"""

	debug("Processing #{0} - {1}".format(key, "Forward pass" if not backwardPass else "Backward pass"))

	# set start time
	# start = startTimer()

	# sync current folder
	sync(PATH_SRC, PATH_DEST, "sync", logger=mylogger.logger, twoway=False, create=True, purge=purge, verbose=True)

	# info("{0} seconds to update files".format(stopTimer(start)))

def formatDateTime(format):
	"""Return a formated date/time depending on format"""
	return time.strftime(format, time.localtime())

def clearScreen():
	"""Clear the user screen (important when not run as daemon)"""
	if os.name == "nt":
		# windows
		os.system("cls")
	else:
		# linux
		os.system("clear")
