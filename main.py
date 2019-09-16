# -*- coding: utf-8 -*-
# This program copies file from the source directory 
# to the destination directory
# Author : Anwar Buchoo (luckyhuss@msn.com)
# Date : 16-Sep-2016
# Version : 1.1

# Import dirsync for the sync functionality

import mylogger
import utils


class SyncObject:
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest

syncPath = dict([
	("1", SyncObject("C:/temp/src", "C:/temp/dest")),
	("2", SyncObject("C:/temp/src", "C:/temp/dest1"))
])

def main():

	# initialise application
	initialise()

	for key in syncPath.keys():
		print("f : {0} - ".format(syncPath[key].src) + syncPath[key].dest)
		# source path
		PATH_SRC = syncPath[key].src
		# destination path
		PATH_DEST = syncPath[key].dest
		utils.directorySync(PATH_SRC, PATH_DEST)

	utils.info("Exiting program")


def initialise():
	utils.clearScreen()
	mylogger.initLogging()
	utils.info("Starting program")

	#utils.info("Starting program with BASE : {0}".format(utils.PATH_BASE))

# call main function
main()