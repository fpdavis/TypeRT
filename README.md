# TypeRT
Displays the contents of a text file or files. 

	This tool is similar to the DOS command type but inspired by old school text typing presentations where text appeared as if someone were typing it in Real Time (hence the name). Usually these presentations would be accompanied by music, ASCII art, and colored text.

Example Uses

	TypeRT

Installation

	This tool is written in Python (https://www.python.org). You must have a recent version of Python installed and in your environment path. You should also have the extension ".py" associated with Python.
	
	Place the file TypeRT.py in any location of your choosing. I recommend a location that is in your PATH environment variable so you will need to type the full path of the file to run it. A good location is in your Python directory under "Scripts".


Todo (in order of importance):

   * Read in command line arguments
   * Should support the following command line arguments… 
        --help|-h|/?  – Displays the proper usage of the application including any command line parameters.
        --KEY=X       – Any key in the the .config file may be overridden via this command. 
		                KEY is the corresponding name of the key in the .config file.
   * Should have a DisplayUsage Method that prints to the console the proper way to invoke the application
   * Should provide the begin time, end time, and run time 
   * Create a config file?
   * Write RTRecorder, perhaps as plugins for popular editors?
   * Write support for RTRecorder files
   
   
Changes (oldest to newest):

   * Commit to Github
   * Create comment sections
   * Create readme file