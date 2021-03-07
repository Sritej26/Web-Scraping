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
	npath=path+"/Chattisgarh"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)

def registrar():
	url="http://clists.nic.in/ddir/PDFCauselists/chattisgarh/2019/%s/060%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Registrar List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Chattisgarh/Registrar List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def weekly():
	url="http://clists.nic.in/ddir/PDFCauselists/chattisgarh/2019/%s/012%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Weekly List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Chattisgarh/Weekly List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def supplementary():
	url="http://clists.nic.in/ddir/PDFCauselists/chattisgarh/2019/%s/011%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Supplementary List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Chattisgarh/Supplementary List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def dailyList():
	url="http://clists.nic.in/ddir/PDFCauselists/chattisgarh/2019/%s/013%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Daily List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Chattisgarh/Daily List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def main():
	dailyList()
	supplementary()
	weekly()
	registrar()
if __name__=="__main__":
	main()
