import os
import sys
import time
import random
from itertools import chain
from datetime import timedelta
from enum import Enum  

# ToDo:
#   * Commit to Github
#   * Create comment sections
#   * Create readme file
#   * Should have a DisplayUsage Method that prints to the console the proper way to invoke the application
#   * Should provide the begin time, end time, and run time 
#   * Read in command line arguments
#   * Should support the following command line arguments… 
#      --help|-h|/?  – Displays the proper usage of the application including any command line parameters.
#      --KEY=X       – Any key in the appSettings section of the .config file may be overridden via this command. KEY is the corresponding name of the key in the .config file.
#   * Write RTRecorder, perhaps as plugins for popular editors?
#   * Write support for RTRecorder files

saRootDirectories = ["c:/"]
saEndsWith = [".csv", ".bat"]
fTimeToSleep = 1
fLow = -.5
fHigh = .3
fMaxSleepTime = 1
saFileList = []
sFileToType = "" #"c:/OneDrive/Applications/Python/Lib/venv/scripts/nt/activate.bat"

# Support for Verbosity levels for information dense applications.
#   * Debug - Super detail
#   * Verbose – Everything Important
#   * Information - Updates that might be useful to user
#   * Warning - Bad things that happen, but are expected
#   * Error - Errors that are recoverable
#   * Critical - Errors that stop execution
goVerbosityEnum = Enum('Verbosity', 'Critical Error Warning Information Verbose Debug')
goVerbosity = goVerbosityEnum.Debug

def main(argv):

    if (len(sFileToType) > 0):
        TypeRTFile(sFileToType)
    else:
        while True:
            
            GetTextFiles(saRootDirectories, saEndsWith)
            for sFile in saFileList:
                TypeRTFile(sFile)
            
            
def GetTextFiles(saRootDirectories, saEndsWith):

    MessageLog ("Getting File List...", goVerbosityEnum.Information)
    oStartTime = time.time()

    for root, dirs, files in chain.from_iterable(os.walk(sRoot) for sRoot in saRootDirectories):
        for oFile in files:
           if (oFile.lower().endswith(tuple(saEndsWith))):
               saFileList.append(os.path.join(root, oFile))
               TypeFastRT(os.path.join(root, oFile), True)

    oEndTime = time.time()
    ElapsedTime = str(timedelta(seconds=oEndTime - oStartTime))  
    MessageLog ("Dirctory obtained in " + ElapsedTime, goVerbosityEnum.Information)
       
def TypeFastRT(sStringToType, newline=False):
    for cCharacter in sStringToType:
        time.sleep(.02) 
        print (cCharacter, end='', flush=True)

    if (newline): print()
    
def TypeRT(sStringToType, newline=False):
    fLocalTimeToSleep = fTimeToSleep # Don't want to modify the global variable
    for cCharacter in sStringToType:
        time.sleep(fLocalTimeToSleep) 
        print (cCharacter, end='', flush=True)
        if (cCharacter == ' '): 
            fLocalTimeToSleep = .1
        else:
            fLocalTimeToSleep += random.uniform(fLow, fHigh)
            if (fLocalTimeToSleep < 0 or fLocalTimeToSleep > fMaxSleepTime): fLocalTimeToSleep = 0

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