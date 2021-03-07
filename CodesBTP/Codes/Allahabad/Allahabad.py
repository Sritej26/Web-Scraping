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
	npath=path+'/Allahabad'		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)

def application():
	link="http://www.allahabadhighcourt.in/clist/AP%s2019_%s_1.pdf"
	directoryCheck("Application List/"+name)
	
	for i in range(1,81):
		url=link%(date,i)
		try:
			page=urllib2.urlopen(url)
			data=page.read()
			with open(path+'/Allahabad/Application List/'+name+'/court'+str(i)+'.pdf','wb') as f:
						f.write(data)
		except:	
			print url
			pass

def supplementary():
	link="http://www.allahabadhighcourt.in/clist/AS%s2019_%s_1.pdf"
	directoryCheck("Supplementary List/"+name)
	
	for i in range(1,81):
		url=link%(date,i)
		try:
			page=urllib2.urlopen(url)
			data=page.read()
			with open(path+'/Allahabad/Supplementary List/'+name+'/court'+str(i)+'.pdf','wb') as f:
						f.write(data)
		except:	
			print url
			pass

def additional():
	url="http://www.allahabadhighcourt.in/clist/AA%s2019_-99_1.pdf"
	url=url%(date)
	directoryCheck("Additional List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Allahabad/Additional List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def fresh():
	url="http://www.allahabadhighcourt.in/clist/AF%s2019_-99_1.pdf"
	url=url%(date)
	directoryCheck("Fresh List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Allahabad/Fresh List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def dailyList():
	url="http://www.allahabadhighcourt.in/clist/AD%s2019_-99_1.pdf"
	url=url%(date)
	directoryCheck("Daily List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Allahabad/Daily List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass

def main():
	dailyList()
	fresh()
	additional()
	supplementary()
	application()
if __name__=="__main__":
	main()
