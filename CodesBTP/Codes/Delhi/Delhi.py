import urllib2
import datetime
import os
from bs4 import BeautifulSoup

x=datetime.datetime.now()
month=x.strftime("%b")
date=x.strftime("%d")+x.strftime("%m")
name=x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y")
dDate=x.strftime("%d")+"."+x.strftime("%m")+"."+x.strftime("%Y")

links=[]

with open('information.txt', 'r') as f:
    lines = f.readlines()

path=lines[0].rstrip()

def download(url,folder):
	try:
		pdfPage=urllib2.urlopen(url)
		pdfData=pdfPage.read()

		directoryCheck(folder)

		with open(path+'/Delhi/'+folder+'/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass

def extractLinks():
	url="http://delhihighcourt.nic.in/causelist_NIC_PDF.asp"

	pdfPage=urllib2.urlopen(url)
	soup=BeautifulSoup(pdfPage,features="html.parser")

	divDataEven=soup.findAll('li',attrs={'class': 'clearfix  even '})
	divDataOdd=soup.findAll('li',attrs={'class': 'clearfix  odd '})

	for div in divDataEven:
		url2="http://delhihighcourt.nic.in/"+div.find('a').get('href')
		links.append(url2)
	for div in divDataOdd:
		url2="http://delhihighcourt.nic.in/"+div.find('a').get('href')
		links.append(url2)

def directoryCheck(state):
	npath=path+"/Delhi"
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)
def advance():
	url="http://delhihighcourt.nic.in/causelist_NIC_PDF.asp"
	stmt="Advance Cause List for "+dDate

	pdfPage=urllib2.urlopen(url)
	soup=BeautifulSoup(pdfPage,features="html.parser")

	divDataEven=soup.findAll('li',attrs={'class': 'clearfix  even '})
	divDataOdd=soup.findAll('li',attrs={'class': 'clearfix  odd '})
	divData=divDataEven+divDataOdd
	var=0
	for div in divData:
		spanData=div.find('span')
		Data=spanData.string.extract().strip()

		if stmt==Data:
			download(links[var],"Advance List")
		var=var+1

def preLokAdalat():
	url="http://delhihighcourt.nic.in/causelist_NIC_PDF.asp"
	stmt="Pre Lok Adalat Cause List for "+dDate

	pdfPage=urllib2.urlopen(url)
	soup=BeautifulSoup(pdfPage,features="html.parser")

	divDataEven=soup.findAll('li',attrs={'class': 'clearfix  even '})
	divDataOdd=soup.findAll('li',attrs={'class': 'clearfix  odd '})
	divData=divDataEven+divDataOdd
	var=0
	for div in divData:
		spanData=div.find('span')
		Data=spanData.string.extract().strip()

		if stmt==Data:
			download(links[var],"Pre Lok Adalat List")
		var=var+1
def regular():
	url="http://delhihighcourt.nic.in/causelist_NIC_PDF.asp"
	stmt="Regular Cause List for "+dDate

	pdfPage=urllib2.urlopen(url)
	soup=BeautifulSoup(pdfPage,features="html.parser")

	divDataEven=soup.findAll('li',attrs={'class': 'clearfix  even '})
	divDataOdd=soup.findAll('li',attrs={'class': 'clearfix  odd '})
	divData=divDataEven+divDataOdd
	var=0
	for div in divData:
		spanData=div.find('span')
		Data=spanData.string.extract().strip()

		if stmt==Data:
			download(links[var],"Regular List")
		var=var+1
def dailyList():
	url="http://delhihighcourt.nic.in/causelist_NIC_PDF.asp"
	stmt="Cause List for "+dDate

	pdfPage=urllib2.urlopen(url)
	soup=BeautifulSoup(pdfPage,features="html.parser")

	divDataEven=soup.findAll('li',attrs={'class': 'clearfix  even '})
	divDataOdd=soup.findAll('li',attrs={'class': 'clearfix  odd '})
	divData=divDataEven+divDataOdd
	var=0
	for div in divData:
		spanData=div.find('span')
		Data=spanData.string.extract().strip()

		if stmt==Data:
			download(links[var],"Daily List")
		var=var+1

def main():
	extractLinks()
	dailyList()
	regular()
	preLokAdalat()
	advance()
if __name__=="__main__":
	main()
