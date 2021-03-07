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
	npath=path+"/Madras"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)

def miscList():
	links=[]
	#url="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%2001%202019%20{3}.pdf"
	#links.append(url.format(month,date,x.strftime("%d"),"misc"))
	#links.append(url.format(month,date,x.strftime("%d"),"MISC"))
	#url2="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%2002%202019%20{3}.pdf"
	#links.append(url2.format(month,date,x.strftime("%d"),"misc"))
	#links.append(url2.format(month,date,x.strftime("%d"),"MISC"))
	#url3="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%2002%202019%20new%20{3}.pdf"
	#links.append(url3.format(month,date,x.strftime("%d"),"misc"))
	#links.append(url3.format(month,date,x.strftime("%d"),"MISC"))
	#url4="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%2002%202018%20new%20{3}.pdf"
	#links.append(url4.format(month,date,x.strftime("%d"),"misc"))
	#links.append(url4.format(month,date,x.strftime("%d"),"MISC"))
	#url5="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%20{3}.pdf"
	#links.append(url5.format(month,date,"misc",x.strftime("%d")))
	#links.append(url5.format(month,date,"MISC",x.strftime("%d")))
	url="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%20{3}%202019%20{4}.pdf"
	url4="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%20{3}%202019%20c%20{4}.pdf"
	url9="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%20{3}%202019%20%{4}.pdf"
	url2="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%20{3}%202019%20new%20{4}.pdf"
	url6="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%20{3}%202019%20NEW%20{4}.pdf"
	url3="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019MISC%20{2}.pdf"
	url5="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%20{3}%202019%20n%20misc.pdf"
	url7="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}{3}%20new.pdf"
	url8="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/032{1}2019{2}%20{3}%202019%20misc.pdf"
	links.append(url.format(month,date,x.strftime("%d"),x.strftime('%m'),'MISC'))
	links.append(url.format(month,date,x.strftime("%d"),x.strftime('%m'),'Misc'))
	links.append(url.format(month,date,x.strftime("%d"),x.strftime('%m'),'misc'))
	links.append(url4.format(month,date,x.strftime("%d"),x.strftime('%m'),'Misc'))
	links.append(url4.format(month,date,x.strftime("%d"),x.strftime('%m'),'misc'))
	links.append(url9.format(month,date,x.strftime("%d"),x.strftime('%m'),'misc'))
	links.append(url2.format(month,date,x.strftime("%d"),x.strftime('%m'),'MISC'))
	links.append(url2.format(month,date,x.strftime("%d"),x.strftime('%m'),'misc'))
	links.append(url6.format(month,date,x.strftime("%d"),x.strftime('%m'),'misc'))
	links.append(url3.format(month,date,x.strftime("%d")))
	links.append(url3.format(month,date,x.strftime("%d")))
	links.append(url5.format(month,date,x.strftime("%d"),x.strftime("%m")))
	links.append(url7.format(month,date,"misc",x.strftime("%d")))
	links.append(url8.format(month,date,x.strftime("%d"),x.strftime("%m")))
	directoryCheck("Misc List")
	for link in links:
		try:
			page=urllib2.urlopen(link)
			data=page.read()
			with open(path+'/Madras/Misc List/'+name+'.pdf','wb') as f:
						f.write(data)
		except:
			print link
			pass

def sitting():
	links=[]
	#url2="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/ST_030{1}2019{2}%20{3}%202018%20{4}.pdf"
	#url4="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/ST_030{1}2019{2}%20{3}.pdf"
	
	url="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/ST_030{1}2019{2}%20{3}%202019%20{4}.pdf"
	url1="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/ST_030{1}2019{2}%20{3}.pdf"
	url2="http://clists.nic.in/ddir/PDFCauselists/madras/2019/{0}/ST_030{1}2019{2}%20{3}.pdf"
	
	links.append(url.format(month,date,x.strftime("%d"),x.strftime("%m"),"sitting"))
	links.append(url.format(month,date,x.strftime("%d"),x.strftime("%m"),"SITTING"))
	links.append(url2.format(month,date,month.upper(),x.strftime("%d")))
	links.append(url2.format(month,date,month.upper(),x.strftime("%d")))
	links.append(url1.format(month,date,x.strftime("%B").upper(),x.strftime("%d")[1]))		
	#links.append(url2.format(month,date,x.strftime("%d"),x.strftime("%m"),"sitting"))
	#links.append(url2.format(month,date,x.strftime("%d"),x.strftime("%m"),"SITTING"))
	#links.append(url4.format(month,date,month.upper(),x.strftime("%d")))
	directoryCheck("Sitting List")
	
	for link in links:
		try:
			page=urllib2.urlopen(link)
			data=page.read()
			with open(path+'/Madras/Sitting List/'+name+'.pdf','wb') as f:
						f.write(data)
		except:
			print link
			pass
def dailyList():
	url="http://clists.nic.in/ddir/PDFCauselists/madras/2019/%s/013%s2019.pdf"
	url=url%(month,date)
	directoryCheck("Daily List")
	try:
		page=urllib2.urlopen(url)
		data=page.read()
		with open(path+'/Madras/Daily List/'+name+'.pdf','wb') as f:
					f.write(data)
	except:
		print url
		pass
def main():
	dailyList()
	sitting()
	miscList()
if __name__=="__main__":
	main()
