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
	npath=path+"/Jharkhand"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)

def supplementary():
	links=[
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019SUPPLEMENTARY_CAUSELIST_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019NEW_SUPPLEMENTARY_CAUSELIST_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019SUPPLEMENTARY_CAUSELIST_NEW_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019SUPPLEMENTARY_CAUSELIST_FINAL_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019Supplementary_New_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019Supplementary_causelist_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019SUPPLEMENTARY_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019supplementary_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/011%s2019supplementary_causelist_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019DAILY_CAUSELIST_%s2019.pdf"
	]
	for url in links:
		url=url%(month,date,date)
		directoryCheck("Supplementary List")
		try:
			page=urllib2.urlopen(url)
			data=page.read()
			with open(path+'/Jharkhand/Supplementary List/'+name+'.pdf','wb') as f:
						f.write(data)
		except:
			print url
			pass
def dailyList():
	links=[
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019Daily_causelist_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019daily_causelist_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019DAILY_CAUSELIST_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019DAILYCAUSELIST_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019NEW_DAILY_CAUSELIST_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019DAILY_CAUSELIST_FINAL_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019DAILY_FINAL_2_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019DAILY_CAUSELIST_NEW_%s2019.pdf",
	"http://clists.nic.in/ddir/PDFCauselists/jharkhand/2019/%s/013%s2019DAILY_CAUSELIST__NEW_%s2019.pdf"
	]
	
	for url in links:
		url=url%(month,date,date)
		directoryCheck("Daily List")
		try:
			page=urllib2.urlopen(url)
			data=page.read()
			with open(path+'/Jharkhand/Daily List/'+name+'.pdf','wb') as f:
						f.write(data)
		except:
			print url
			pass

def main():
	dailyList()
	supplementary()

if __name__=="__main__":
	main()
