import urllib2
import datetime
import re
import os
from bs4 import BeautifulSoup

x=datetime.datetime.now()
date=x.strftime("%d")+"-"+x.strftime("%m")
month=x.strftime("%b")
name=x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y")

with open('information.txt', 'r') as f:
    lines = f.readlines() 

path=lines[0].rstrip()

def directoryCheck(state):
	npath=path+"/Gauhati"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)


def lawazima():
	url="http://www.ghconline.gov.in/NewCList/lz-%s-2019.pdf"
	url=url%(date)
	
	try:
		htmlPage=urllib2.urlopen(url)
		htmlData=htmlPage.read()
			
		directoryCheck("/Lawazima List")
			
		with open(path+'/Gauhati/Lawazima List/'+name+'.pdf','wb') as f:
				f.write(htmlData)
	except:
		print url
		pass

def supplementary():
	url="http://www.ghconline.gov.in/NewCList/sl-%s-2019.pdf"
	url=url%(date)
	
	try:
		htmlPage=urllib2.urlopen(url)
		htmlData=htmlPage.read()
			
		directoryCheck("/Supplementary List")
			
		with open(path+'/Gauhati/Supplementary List/'+name+'.pdf','wb') as f:
				f.write(htmlData)
	except:
		print url
		pass

def dailyList():
	url="http://www.ghconline.gov.in/NewCList/dl-%s-2019.pdf"
	url=url%(date)
	
	try:
		htmlPage=urllib2.urlopen(url)
		htmlData=htmlPage.read()
			
		directoryCheck("/Daily List")
			
		with open(path+'/Gauhati/Daily List/'+name+'.pdf','wb') as f:
				f.write(htmlData)
	except:
		print url
		pass
		

def main():
	dailyList()
	supplementary()
	lawazima()
if __name__=="__main__":
	main()
