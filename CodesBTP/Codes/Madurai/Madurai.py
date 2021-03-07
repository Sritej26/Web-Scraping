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
	npath=path+"/Madurai"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)


def advance():
	url="http://clists.nic.in/ddir/PDFCauselists/madurai/2019/%s/010%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Advance List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Madurai/Advance List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass


def miscList():
	url="http://clists.nic.in/ddir/PDFCauselists/madurai/2019/%s/032%s2019MISC.pdf"
	url2="http://clists.nic.in/ddir/PDFCauselists/madurai/2019/{0}/032{1}2019{2}2019%20misc.pdf"
	url3="http://clists.nic.in/ddir/PDFCauselists/madurai/2019/%s/032%s2019%s2019.pdf"
	url4="http://clists.nic.in/ddir/PDFCauselists/madurai/2019/{0}/032{1}2019misc%20merge%20{2}2019.pdf"
	url5="http://clists.nic.in/ddir/PDFCauselists/madurai/2019/%s/032%s2019MISC%s2019.pdf"
	url=url%(month,date)
	url2=url2.format(month,date,date)
	url3=url3%(month,date,date)
	url4=url4.format(month,date,date)
	url5=url5%(month,date,date)
	directoryCheck("Misc List")
	links=[]
	links.append(url)
	links.append(url2)
	links.append(url3)
	links.append(url4)
	links.append(url5)
	for link in links:
		try:
			page=urllib2.urlopen(link)
			data=page.read()
			with open(path+'/Madurai/Misc List/'+name+'.pdf','wb') as f:
						f.write(data)
		except:
			print url
			pass


def sitting():
	links=[]
	url="http://clists.nic.in/ddir/PDFCauselists/madurai/2019/%s/ST_030%s2019SITTING.pdf"
	url=url%(month,date)
	directoryCheck("Sitting List")
	
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Madurai/Sitting List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def dailyList():
	url="http://clists.nic.in/ddir/PDFCauselists/madurai/2019/%s/013%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Daily List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Madurai/Daily List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def main():
	dailyList()
	sitting()
	miscList()
	advance()
if __name__=="__main__":
	main()
