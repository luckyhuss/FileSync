# -*- coding: utf-8 -*-
# This program provides utility functions
# Author : Anwar Buchoo (luckyhuss@msn.com)
# Date : 16-Sep-2016
# Version : 1.0

import io
import os
import time
from contextlib import redirect_stdout

from dirsync import sync

import mylogger

# application paths
PATH_BASE = os.path.dirname(os.path.realpath(__file__))
PATH_LOG = os.path.normpath(PATH_BASE + "/logs")

# application files
FILE_LOG = os.path.normpath(PATH_LOG + "/main.log")

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



def directorySync(PATH_SRC, PATH_DEST):
	"""Sync the folders"""

	debug("{0} {1}".format(PATH_SRC, PATH_DEST))

	# set start time
	start = startTimer()

	f = io.StringIO()
	with redirect_stdout(f):
		sync(PATH_SRC, PATH_DEST, "sync", purge=False, verbose=True)
	out = f.getvalue()

	info("\r\n" + out)

	info("{0} seconds to update albums error".format(stopTimer(start)))

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

def bool(value):
	"""Convert a value (yes|true|t|1) to bool"""
	# cast to string
	value = str(value)
	return value.lower() in ("yes", "true", "t", "1")
