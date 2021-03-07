import urllib2
import datetime
import re
import os
from BeautifulSoup import BeautifulSoup
from selenium import webdriver
import time
import ssl

# For obtaining the date and month from device
x=datetime.datetime.now()
month=x.strftime("%b")
date=x.strftime("%d")+x.strftime("%m")
name=x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y")
Gdate=x.strftime("%d")+"-"+x.strftime("%m")
Cdate=x.strftime("%m")+"_"+x.strftime("%d")
Jdate=x.strftime("%d")+"_"+x.strftime("%m")
Hdate=x.strftime("%m")+x.strftime("%d")


with open('information.txt', 'r') as f:
    lines = f.readlines() 

path=lines[0].rstrip()
dpath=lines[1].rstrip()
cpath=lines[2].rstrip()


def directoryCheck(state):
	#path="/home/sailok/Desktop/BTP Data"		
	fpath=path+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(path+'/'+state)


#Download function for downloading the pdf data
def download(url):
	try:
		pdfPage=urllib2.urlopen(url)
		pdfData=pdfPage.read()
	
		lists=[]
		for match in re.finditer('/',url):
			lists.append(match.start())
	
		state=url[lists[4]+1:lists[5]]
		state=state[0].upper()+state[1:len(state)].lower()

		print state+':'
		
		directoryCheck(state)
		
		with open(path+'/'+state+'/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass

#Download function for downloading the pdf data
def diffDownload(url,state):
	print state+':'
	try:
		pdfPage=urllib2.urlopen(url)
		pdfData=pdfPage.read()
		
		directoryCheck(state)
		
		with open(path+'/'+state+'/'+name+'.pdf','wb') as f:
				f.write(pdfData)
	except:
		print url
		pass

#Download function for downloading the pdf data of J/K HC
def jammuSri(url,state):
	print state+':'
	url2="http://www.jkhighcourt.nic.in/"
	pdfPage=urllib2.urlopen(url)
	soup=BeautifulSoup(pdfPage)
	
	divData=soup.find('div',attrs={'class': ' welcome'})
	url2+=divData.find('a').get('href').replace('\\','/')
	
	urlDate=divData.find('a')
	urlDate.img.decompose()
	urlDate=urlDate.string.extract()	
	
	currentDate=x.strftime("%d")+"-"+x.strftime("%m")+"-"+x.strftime("%Y")

	if currentDate in urlDate:
		url2=url2.replace(' ','%20')
		diffDownload(url2,state)	

def main():
	f=open("clistWebsites.txt","r")
	for line in f:
		if line!="\n":
			if "uttarakhand" in line:
				if "KHULBE" in line:
					url=line.format(month,date,date)
					download(url)
				elif "of" in line:
					url=line%(month,date,date)
					download(url)
				elif "om" in line: 
					url=line%(month,date,date)
					download(url)
				elif "ot" in line: 
					url=line%(month,date,date)
					download(url)
				elif "oh" in line: 
					url=line%(month,date,date)
					download(url)
				elif "ow" in line: 
					url=line%(month,date,date)
					download(url)
				elif "oh" in line: 
					url=line%(month,date,date)
					download(url)
				else:
					day=x.strftime("%a")
					url=line%(month,date,day[0],date,9)
					download(url)
					url=line%(month,date,day[0],date,8)
					download(url)
					if day=="Thu":
						url=line%(month,date,day[1].upper(),date,9)
						download(url)
			elif "jk" and "php" in line:
				hdh=333
				jammuSri(line%('j'),"Jammu")
				jammuSri(line%('k'),"Srinagar")
			elif "jmu" in line:
				url=line%(Jdate)
				diffDownload(url,"Jammu")
			elif "sgr" in line:
				url=line%(date)
				diffDownload(url,"Srinagar")
			else:
				url=line%(month,date)
				download(url)	
		
if __name__=="__main__":
	main()
