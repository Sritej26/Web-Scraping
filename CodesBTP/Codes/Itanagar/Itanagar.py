import urllib2
import datetime
import re
import os
from bs4 import BeautifulSoup

x=datetime.datetime.now()
date=x.strftime("%d")+x.strftime("%m")
month=x.strftime("%b")
name=x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y")

aDate=datetime.datetime.strptime(x.strftime("%x"),"%m/%d/%y")
d=datetime.timedelta(days=4)
fDate=aDate+d	
end=fDate.strftime("%d")+fDate.strftime("%m")

with open('information.txt', 'r') as f:
    lines = f.readlines() 

path=lines[0].rstrip()

def directoryCheck(state):
	npath=path+"/Itanagar"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)



def hearing():
	url="http://clists.nic.in/ddir/PDFCauselists/itanagar/2019/%s/031%s2019wk%s%s2019.pdf"
	url=url%(month,date,date,end)
	directoryCheck("Hearing List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Itanagar/Hearing List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def dailyList():
	url="http://clists.nic.in/ddir/PDFCauselists/itanagar/2019/%s/013%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Daily List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Itanagar/Daily List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def main():
	dailyList()
	hearing()
if __name__=="__main__":
	main()
