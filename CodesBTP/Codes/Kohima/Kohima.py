import urllib2
import datetime
import re
import os
from bs4 import BeautifulSoup

x=datetime.datetime.now()
date=x.strftime("%d")+x.strftime("%m")
month=x.strftime("%b")
name=x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y")
date1=x.strftime("%d")+"-"+x.strftime("%m")
date2=x.strftime("%d")+"-"+x.strftime("%m")[1]

with open('information.txt', 'r') as f:
    lines = f.readlines() 

path=lines[0].rstrip()


def directoryCheck(state):
	npath=path+"/Kohima"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)



def weekly():
	url="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/{0}/012{1}2019Hearing%20{2}%2020190001.pdf"
	url=url.format(month,date,month)
	directoryCheck("Weekly List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Kohima/Weekly List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def dailyList():
	links=[]
	url="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/%s/013%s2019%s-20190001.pdf"
	url2="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/{0}/013{1}2019Causelist%20{2}-2019.pdf"
	url3="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/%s/013%s2019-%s-20190001.pdf"
	url4="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/{0}/013{1}2019causelist%20{2}-2019.pdf"	
	url9="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/{0}/013{1}2019{2}-2019%20causelist.pdf"
	url5="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/{0}/013{1}2019causelist%20-{2}-20190001.pdf"
	url6="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/%s/013%s2019%s2019.pdf"
	url7="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/%s/013%s2019%s-2019.pdf"
	#url8="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/%s/013%s201913%s2019.pdf"
	url8="http://clists.nic.in/ddir/PDFCauselists/kohima/2019/{0}/013{1}2019{2}-2019%20Cause%20list.pdf"
	links.append(url%(month,date,date1))
	links.append(url%(month,date,date2))
	links.append(url3%(month,date,date1))
	links.append(url3%(month,date,date2))
	links.append(url2.format(month,date,date1))
	links.append(url4.format(month,date,date1))
	links.append(url9.format(month,date,date1))
	links.append(url5.format(month,date,date1))
	links.append(url6%(month,date,date))
	links.append(url7%(month,date,date1))
	links.append(url8.format(month,date,date1))
	#links.append(url8%(month,date,x.strftime("%m")))
	directoryCheck("Daily List")
	for link in links:
		try:
			page=urllib2.urlopen(link)
			data=page.read()
			with open(path+'/Kohima/Daily List/'+name+'.pdf','wb') as f:
					f.write(data)
		except:
			print link
			pass

def main():
	dailyList()
	weekly()
if __name__=="__main__":
	main()
