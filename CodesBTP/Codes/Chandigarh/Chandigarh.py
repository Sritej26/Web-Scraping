import urllib2
import datetime
import re
import os
from bs4 import BeautifulSoup
import ssl

x=datetime.datetime.now()
date=x.strftime("%m")+"_"+x.strftime("%d")
month=x.strftime("%b")
name=x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y")


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with open('information.txt', 'r') as f:
    lines = f.readlines() 

path=lines[0].rstrip()

def directoryCheck(state):
	npath=path+"/Chandigarh"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)



def lokAdalatMain():
	state="Chandigarh"
	
	url="https://www.highcourtchd.gov.in/data/2019_%s_l_m.pdf"
	url=url%(date)
	
	try:
		pdfPage=urllib2.urlopen(url,context=ctx)
		pdfData=pdfPage.read()
			
		directoryCheck("Lok Adalat Main")
			
		with open(path+'/'+state+'/Lok Adalat Main/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass
def lokAdalatSup():
	state="Chandigarh"
	
	url="https://www.highcourtchd.gov.in/data/2019_%s_l_s.pdf"
	url=url%(date)
	
	try:
		pdfPage=urllib2.urlopen(url,context=ctx)
		pdfData=pdfPage.read()
			
		directoryCheck("Lok Adalat Sup")
			
		with open(path+'/'+state+'/Lok Adalat Sup/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass
def ordinaryMain():
	state="Chandigarh"
	
	url="https://www.highcourtchd.gov.in/data/2019_%s_o_m.pdf"
	url=url%(date)
	
	try:
		pdfPage=urllib2.urlopen(url,context=ctx)
		pdfData=pdfPage.read()
			
		directoryCheck("Ordinary Main")
			
		with open(path+'/'+state+'/Ordinary Main/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass
def ordinarySup():
	state="Chandigarh"
	
	url="https://www.highcourtchd.gov.in/data/2019_%s_o_s.pdf"
	url=url%(date)
	
	try:
		pdfPage=urllib2.urlopen(url,context=ctx)
		pdfData=pdfPage.read()
			
		directoryCheck("Ordinary Sup")
			
		with open(path+'/'+state+'/Ordinary Sup/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass
def regular():
	state="Chandigarh"
	
	url="https://www.highcourtchd.gov.in/data/2019_%s_r_s.pdf"
	url=url%(date)
	
	try:
		pdfPage=urllib2.urlopen(url,context=ctx)
		pdfData=pdfPage.read()
			
		directoryCheck("Regular")
			
		with open(path+'/'+state+'/Regular/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass
def complete():
	state="Chandigarh"
	
	url="https://www.highcourtchd.gov.in/data/2019_%s_b_m.pdf"
	url=url%(date)
	
	try:
		pdfPage=urllib2.urlopen(url,context=ctx)
		pdfData=pdfPage.read()
			
		directoryCheck("Complete")
			
		with open(path+'/'+state+'/Complete/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass
	
def main():
	complete()
	regular()
	ordinarySup()
	ordinaryMain()
	lokAdalatSup()
	lokAdalatMain()

if __name__=="__main__":
	main()
