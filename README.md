# TypeRT
Displays the contents of a text file or files. 

This tool is similar to the DOS command type but inspired by old school text typing presentations where text appeared as if someone were typing it in Real Time (hence the name). Usually these presentations would be accompanied by music, ASCII art, and colored text.

### Example Uses

	Usage: TypeRT.py [-h] [-c] [-r ROOTDIRECTORIES] [-e ENDSWITH] [-t TIMETOSLEEP]
                 [--Low LOW] [--High HIGH] [-m MAXSLEEPTIME]
                 [-v [{Critical,Error,Warning,Information,Verbose,Debug}]]
                 [File [File ...]]

	Positional Arguments:
	
		File                  Path to file to display

	Optional Arguments:
	
		-h, --help          Show this help message and exit
		-c, --Crawl         Crawl the file system starting in the RootDirectories
							for files ending in EndsWith to display (default: False)
		-r ROOTDIRECTORIES, --RootDirectories ROOTDIRECTORIES
							Root directories to start search for files in (default: ['c:/'])
		-e ENDSWITH, --EndsWith ENDSWITH
							File extensions to search for and display (default: ['.txt', '.csv', '.bat'])
		-t TIMETOSLEEP, --TimeToSleep TIMETOSLEEP
							Initial time to sleep on each line (default: 1)
		--Low LOW           Low end of range to select sleep time from (default: -0.5)
		--High HIGH         High end of range to select sleep time from (default: 0.3)
		-m MAXSLEEPTIME, --MaxSleepTime MAXSLEEPTIME
							Maximum time to sleep, if this is reached TimeToSleep
							is reset to 0 (default: 1)
		-v [{Critical,Error,Warning,Information,Verbose,Debug}], --Verbosity [{Critical,Error,Warning,Information,Verbose,Debug}]
							Verbosity level to display (default: Debug)

### Installation

This tool is written in Python (https://www.python.org). You must have a recent version of Python installed and in your environment path. You should also have the extension ".py" associated with Python.
	
Place the file TypeRT.py in any location of your choosing. I recommend a location that is in your PATH environment variable so you will need to type the full path of the file to run it. A good location is in your Python directory under "Scripts".


### Todo (in order of importance):

   * Display from standard input (UNIX style pipes)
   * Read in config values from a specified file
   * Auto update - who doesn't love auto updates!
   * Write RTRecorder, perhaps as plugins for popular editors?
   * Add sound
   * Write support for RTRecorder files
   
   
### Changes (oldest to newest):

   * Commit to Github
   * Create comment sections
   * Create readme file
   
   * Read in command line arguments
   * Should support the following command line arguments… 
        --help|-h|/?  – Displays the proper usage of the application including any command line parameters.
        --KEY=X       – Any key in the the .config file may be overridden via this command. 
		                KEY is the corresponding name of the key in the .config file.
   * Should have a DisplayUsage Method that prints to the console the proper way to invoke the application
   * Create a config file? - No need to complicate install with a config file. Moved default configuration settings
     to top of the file. Though I could still be talked into adding the ability to read in default values from an
	 external config file.
   * Should provide the begin time, end time, and run time 
