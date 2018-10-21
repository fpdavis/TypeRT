##############################################################################
# Begin Global Config Settings
#
# These values are set to the default values and may be changed as needed.
#
##############################################################################
gsaRootDirectories = ["c:/"]
gsaEndsWith = [".txt", ".csv", ".bat"]
gfTimeToSleep = 1
gfLow = -.5
gfHigh = .3
gfMaxSleepTime = 1

##############################################################################
# End of Global Config Settings
##############################################################################
#
# Updates can be found at https://github.com/fpdavis/TypeRT
#
##############################################################################

import os
import sys
import time
import random
import argparse
from itertools import chain
from datetime import timedelta
from enum import Enum  

##############################################################################
#
# Support for Verbosity levels for information dense applications.
#   * Debug - Super detail
#   * Verbose – Everything Important
#   * Information - Updates that might be useful to user
#   * Warning - Bad things that happen, but are expected
#   * Error - Errors that are recoverable
#   * Critical - Errors that stop execution
#
##############################################################################
goVerbosityEnum = Enum('Verbosity', 'Critical Error Warning Information Verbose Debug')
goVerbosity = goVerbosityEnum.Debug

gsaFileList = []

def main(argv):

    global goVerbosity, gsaEndsWith, gfTimeToSleep, gfLow, gfHigh, gfMaxSleepTime
    
    oStartTime = time.time()
        
    # construct the argument parse and parse the arguments
    oArgumentParser = argparse.ArgumentParser()
    oArgumentParser.add_argument('files', metavar='File', type=argparse.FileType('r'), nargs='*', help="Path to file to display")

    oArgumentParser.add_argument("-c", "--Crawl", required=False, action='store_true', help="Crawl the file system starting in the RootDirectories for files ending in EndsWith to display (default: %(default)s)")
    oArgumentParser.add_argument("-r", "--RootDirectories", required=False, default=gsaRootDirectories, help="Root directories to start search for files in (default: %(default)s)")
    oArgumentParser.add_argument("-e", "--EndsWith", required=False, default=gsaEndsWith, help="File extensions to search for and display (default: %(default)s)")

    oArgumentParser.add_argument("-t", "--TimeToSleep", required=False, type=float, default=gfTimeToSleep, help="Initial time to sleep on each line (default: %(default)s)")
    oArgumentParser.add_argument("--Low", required=False, type=float, default=gfLow, help="Low end of range to select sleep time from (default: %(default)s)")
    oArgumentParser.add_argument("--High", required=False, type=float, default=gfHigh, help="High end of range to select sleep time from (default: %(default)s)")
    oArgumentParser.add_argument("-m", "--MaxSleepTime", required=False, type=float, default=gfMaxSleepTime, help="Maximum time to sleep, if this is reached TimeToSleep is reset to 0 (default: %(default)s)")
    oArgumentParser.add_argument("-v", '--Verbosity', default='Debug', const='Error', nargs='?', choices=goVerbosityEnum._member_names_, help='Verbosity level to display (default: %(default)s)')

    args = vars(oArgumentParser.parse_args())
    
    goVerbosity = goVerbosityEnum[args["Verbosity"]]
    gsaEndsWith = args["EndsWith"]
    gfTimeToSleep = args["TimeToSleep"]
    gfLow = args["Low"]
    gfHigh = args["High"]
    gfMaxSleepTime = args["MaxSleepTime"]

    # Check for standard input
    # if (sys.stdin.isatty()):
    #MessageLog("Displaying standard input line by line...", goVerbosityEnum.Information)
    #for sLine in sys.stdin:
    #    TypeRT(sLine)
    
    if (args["files"] != None and len(args["files"]) > 0):
        for sEachFile in args["files"]:
            MessageLog("Displaying File from command line input...", goVerbosityEnum.Information)
            TypeRT(''.join(sEachFile))
            
    if (args["Crawl"] == True):
        while True:
            GetTextFiles(gsaRootDirectories, gsaEndsWith)
            for sFile in gsaFileList:
                TypeRTFile(sFile)

    oEndTime = time.time()
    MessageLog ("\n\nStart Time: " + time.ctime(oStartTime), goVerbosityEnum.Information)
    MessageLog ("End Time: " + time.ctime(oEndTime), goVerbosityEnum.Information)
    MessageLog ("Elapsed Time: " + str(timedelta(seconds=oEndTime - oStartTime)), goVerbosityEnum.Information)
            
def GetTextFiles(gsaRootDirectories, gsaEndsWith):

    MessageLog ("Getting File List...", goVerbosityEnum.Information)
    oStartTime = time.time()

    for root, dirs, files in chain.from_iterable(os.walk(sRoot) for sRoot in gsaRootDirectories):
        for oFile in files:
           if (oFile.lower().endswith(tuple(gsaEndsWith))):
               gsaFileList.append(os.path.join(root, oFile))
               TypeFastRT(os.path.join(root, oFile), True)

    oElapsedTime = str(timedelta(seconds=time.time() - oStartTime))  
    MessageLog ("Dirctory obtained in " + oElapsedTime, goVerbosityEnum.Information)
       
def TypeFastRT(sStringToType, newline=False):
    for cCharacter in sStringToType:
        time.sleep(.02) 
        print (cCharacter, end='', flush=True)

    if (newline): print()
    
def TypeRT(sStringToType, newline=False):
    fLocalTimeToSleep = gfTimeToSleep # Don't want to modify the global variable
    for cCharacter in sStringToType:
        time.sleep(fLocalTimeToSleep) 
        print (cCharacter, end='', flush=True)
        if (cCharacter == ' '): 
            fLocalTimeToSleep = .1
        else:
            fLocalTimeToSleep += random.uniform(gfLow, gfHigh)
            if (fLocalTimeToSleep < 0 or fLocalTimeToSleep > gfMaxSleepTime): fLocalTimeToSleep = 0

    if (newline): print()
            
def TypeRTFile(sFile):
    MessageLog ("Opening File " + sFile + "...", goVerbosityEnum.Information)
    oFile = open(sFile,"r")

    sStringToType = oFile.read()
    oFile.close()
    TypeRT(sStringToType)

def MessageLog(sMessage, oVerbosity=goVerbosityEnum.Warning):
    if (oVerbosity.value <= goVerbosity.value):
        TypeFastRT(sMessage, True)
            
    
if __name__ == '__main__':
    main(sys.argv)