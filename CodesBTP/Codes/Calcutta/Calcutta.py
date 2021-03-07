import urllib2
import datetime
import re
import os
from bs4 import BeautifulSoup

x=datetime.datetime.now()
date=x.strftime("%d")+x.strftime("%m")
month=x.strftime("%b")
name=x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y")

with open('information.txt', 'r') as f:
    lines = f.readlines()

path=lines[0].rstrip()

def directoryCheck(state):
	npath=path+"/Calcutta"
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)



def appellate():
	url="http://clists.nic.in/ddir/PDFCauselists/calcutta/2019/%s/003%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Appellate List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Calcutta/Appellate List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def dailyList():
	url="http://clists.nic.in/ddir/PDFCauselists/calcutta/2019/%s/002%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Daily List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Calcutta/Daily List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def main():
	dailyList()
	appellate()
if __name__=="__main__":
	main()
