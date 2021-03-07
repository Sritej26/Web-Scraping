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
	npath=path+"/Kerala"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)


def partial():
	url="http://highcourtofkerala.nic.in/causelist/pcl.pdf"
	
	directoryCheck("Partial List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Kerala/Partial List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def roster():
	url="http://highcourtofkerala.nic.in/causelist/dr.pdf"
	
	directoryCheck("Roster List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Kerala/Roster List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def weekly():
	url="http://clists.nic.in/ddir/PDFCauselists/kerala/2019/%s/012%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Weekly List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Kerala/Weekly List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def sitting():
	links=[]
	url="http://clists.nic.in/ddir/PDFCauselists/kerala/2019/%s/ST_030%s2019sitting.pdf"
	url2="http://clists.nic.in/ddir/PDFCauselists/kerala/2019/%s/ST_030%s2019dr.pdf"
	links.append(url%(month,date))
	links.append(url2%(month,date))
	
	directoryCheck("Sitting List")
	for link in links:	
		try:
			page=urllib2.urlopen(link)
			data=page.read()
			with open(path+'/Kerala/Sitting List/'+name+'.pdf','wb') as f:
						f.write(data)
		except:
			print link
			pass
def advance():
	url="http://clists.nic.in/ddir/PDFCauselists/kerala/2019/%s/073%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Advance List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Kerala/Advance List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def dailyList():
	url="http://clists.nic.in/ddir/PDFCauselists/kerala/2019/%s/013%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Daily List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Kerala/Daily List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def main():
	dailyList()
	advance()
	sitting()
	weekly()
	roster()
	partial()
if __name__=="__main__":
	main()
