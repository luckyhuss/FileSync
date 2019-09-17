# -*- coding: utf-8 -*-
# This program copies file from the source directory 
# to the destination directory
# Author : Anwar Buchoo (luckyhuss@msn.com)
# Date : 16-Sep-2016
# Version : 1.1

# Import dirsync for the sync functionality

import io

import mylogger
import utils


class SyncObject:
  def __init__(self, src, dest):
    self.src = src
    self.dest = dest

syncPath = dict([
	("1", SyncObject("C:/Users/ABuchoo.cnslt/Documents/Projects/Veeva", "P:/IT/IT Quality/$ Validation/Working Papers/RFC 8000002427 - Veeva QDocs and RIMS")),
	("2", SyncObject("C:/Users/ABuchoo.cnslt/Documents/Projects/SAP Landscape Simplification", "P:/IT/IT Quality/$ Validation/Working Papers/RFC8000002453 - SAP Landscape Simplification"))
])

def main():

	# initialise application
	initialise()

	for key in syncPath.keys():
		# source path
		PATH_SRC = syncPath[key].src
		# destination path
		PATH_DEST = syncPath[key].dest
		
		# two-way file sync
		# sync all files, in dictionary order
		utils.directorySync(key, PATH_SRC, PATH_DEST, False)
		# sync all files, in dictionary order
		utils.directorySync(key, PATH_DEST, PATH_SRC, True)

	utils.info("Exiting program")

def initialise():
	utils.clearScreen()
	mylogger.initLogging()
	utils.info("Starting program")

	#utils.info("Starting program with BASE : {0}".format(utils.PATH_BASE))

# call main function
main()
