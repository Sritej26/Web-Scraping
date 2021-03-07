Packages required to run the codes
	1) Beautiful Soup
	2) Urllib2
	3) Selenium 
Python 2 version is used, hence all the packages must be downloaded for Python 2 version

Organisation of codes

/Codes
	downloader.py         [script for running all python files]
	information.text	  [where important address are stored]
	/Aizwal				  [Folder for each High court]
		Aizwal.py         [Individual Python script for each High Court]
	/Andhra
		Andhra.py


Before running modify "information.txt"

##################################################################################

In information.txt:
address1  ==> address where causelist will be downloaded [Donot change]
address2  ==> address of downloads folder in local machine [/home/user/downloads]
address3  ==> address of chromedriver [/path/to/chromedriver]

##################################################################################

How to run.
	1) Open terminal in present directory(/Codes) and type "Python2 downloader.py"
	2) Wait until all the causelists are downloaded.