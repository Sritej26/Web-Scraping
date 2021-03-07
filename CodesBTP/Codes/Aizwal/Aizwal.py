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
	npath=path+'/Aizwal'
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)



def hearing():
	links=[]
	url="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/%s/031%s2019hearing.pdf"
	url1="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/%s/031%s2019Hearing.pdf"
	url2="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/031{1}2019db%20hear.pdf"
	url7="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/031{1}20196%20{2}-10%20{3}%202019%20hearing.pdf"
	url3="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/031{1}2019{2}%20hear.pdf"
	links.append(url%(month,date))
	links.append(url1%(month,date))
	links.append(url2.format(month,date))
	links.append(url3.format(month,date,x.strftime("%a").lower()))
	links.append(url7.format(month,date,month,month))
	directoryCheck("Hearing List")
	for link in links:
		try:
			page=urllib2.urlopen(link)
			data=page.read()
			with open(path+'/Aizwal/Hearing List/'+name+'.pdf','wb') as f:
						f.write(data)
		except:
			print link
			pass
def dailyList():
	url="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/%s/013%s2019%s.pdf"
	url9="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019{2}%20Cause.pdf"
	url2="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019{2}%20cause.pdf"
	url3="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019DB%20{2}.pdf"
	url4="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019{2}%20causelist.pdf"
	url5="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019causelist.pdf"
	url6="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/%s/013%s2019%s.pdf"
	#url7="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019{2}.pdf"
	url7="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}20196%20{2}-10%20{3}%202019%20Causelist.pdf"
	url8="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019{2}%20CAUSE.pdf"
	url10="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019DB.pdf"
	url11="http://clists.nic.in/ddir/PDFCauselists/aizwal/2019/{0}/013{1}2019{2}%20Causelist.pdf"

	links=[]

	links.append(url11.format(month,date,x.strftime("%A")))
	day=x.strftime("%a")
	if day=="Thu":
		day+='rs'
	z=url%(month,date,day)
	links.append(z)
	links.append(url%(month,date,day.lower()))
	day+='day'
	z=url9.format(month,date,day)
	links.append(z)

	day=day.lower()
	z=url%(month,date,day)
	links.append(z)

	day=x.strftime("%A")
	day=day.lower()
	z=url%(month,date,day)
	links.append(z)
	links.append(url%(month,date,x.strftime("%A")))
	links.append(url%(month,date,x.strftime("%a")))
	links.append(url%(month,date,date[1]+month.lower()))
	links.append(url%(month,date,date[1]+'%20'+month))
	links.append(url2.format(month,date,x.strftime("%a").lower()))
	links.append(url2.format(month,date,x.strftime("%A").lower()))
	links.append(url2.format(month,date,x.strftime("%d")))
	links.append(url3.format(month,date,x.strftime("%a").lower()))
	links.append(url4.format(month,date,x.strftime("%a").lower()))
	links.append(url5.format(month,date))
	links.append(url6%(month,date,x.strftime("%d")+month))
	links.append(url6%(month,date,x.strftime("%a").lower()))
	links.append(url7.format(month,date,month,month))
	links.append(url8.format(month,date,x.strftime("%a").upper()))
	links.append(url10.format(month,date))
	if x.strftime('%a').lower()=='tue':
		links.append(url6%(month,date,x.strftime('%A').lower()[0:4]))
	directoryCheck("Daily List")
	for link in links:
		try:
			page=urllib2.urlopen(link)
			data=page.read()
			with open(path+'/Aizwal/Daily List/'+name+'.pdf','wb') as f:
						f.write(data)
		except:
			print link
			pass

def main():
	dailyList()
	hearing()
if __name__=="__main__":
	main()
