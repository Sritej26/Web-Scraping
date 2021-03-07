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
	#path="/home/sailok/Desktop/BTP Data/"		
	fpath=path+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(path+'/'+state)


def advance():
	url=[	"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/advconsolidation.htm",
		"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/advdharconsolidation.htm",
		"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/advgulconsolidation.htm"
		]
	state=["Bengaluru","Dharwad","Gulbarga"]
	
	for i in range(3):
		try:
			htmlPage=urllib2.urlopen(url[i])
			htmlData=htmlPage.read()
		
			directoryCheck(state[i]+"/Advance List")
		
			with open(path+'/'+state[i]+'/Advance List/'+name+'.html','wb') as f:
					f.write(htmlData)
		except:
			print state[i]
			pass

def supplementary():
	url=[	"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/supconsolidation.htm",
		"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/supdharconsolidation.htm",
		"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/supgulconsolidation.htm"
		]
	state=["Bengaluru","Dharwad","Gulbarga"]
	
	for i in range(3):
		try:
			htmlPage=urllib2.urlopen(url[i])
			htmlData=htmlPage.read()
		
			directoryCheck(state[i]+"/Supplementary List")
		
			with open(path+'/'+state[i]+'/Supplementary List/'+name+'.html','wb') as f:
					f.write(htmlData)
		except:
			print state[i]
			pass

def dailyList():
	url=[	"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/consolidation.htm",
		"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/dharconsolidation.htm",
		"http://karnatakajudiciary.kar.nic.in/ConsolidatedCauselist/gulconsolidation.htm"
		]
	state=["Bengaluru","Dharwad","Gulbarga"]
	
	for i in range(3):
		try:
			htmlPage=urllib2.urlopen(url[i])
			htmlData=htmlPage.read()
			
			directoryCheck(state[i]+"/Daily List")
			
			with open(path+'/'+state[i]+'/Daily List/'+name+'.html','wb') as f:
					f.write(htmlData)
		except:
			print state[i]
			pass

def main():
	dailyList()
	supplementary()
	advance()
if __name__=="__main__":
	main()
