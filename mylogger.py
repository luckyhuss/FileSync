# This program initialises the logging system
# Author : Anwar Buchoo (luckyhuss@msn.com)
# Date : 16-Sep-2016
# Version : 1.1

import logging
import os
from logging.handlers import TimedRotatingFileHandler

import utils

# logger
logger = logging.getLogger("MyLogger")

def initLogging():
	# build and normalize path for the OS in use
	
	if not os.path.exists(utils.PATH_LOG):
		# create log dir
		os.makedirs(utils.PATH_LOG)
	
	logFileName = utils.FILE_LOG	
	logHandler = TimedRotatingFileHandler(logFileName, when="midnight")
	logFormatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", datefmt="%d-%b-%Y %H:%M:%S")
	logHandler.setFormatter(logFormatter)
	logger.addHandler(logHandler)
	logger.setLevel(logging.DEBUG)
