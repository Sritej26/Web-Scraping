import urllib2
import datetime
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time

x=datetime.datetime.now()
month=x.strftime("%b")
date=x.strftime("%d")+"-"+x.strftime("%m")+"-"+x.strftime("%Y")
name=x.strftime("%d")+" "+x.strftime("%b")+" "+x.strftime("%Y")

with open('information.txt', 'r') as f:
    lines = f.readlines()

path=lines[0].rstrip()
dpath=lines[1].rstrip()
cpath=lines[2].rstrip()

def preference(driver):
	driver.get('chrome://settings/content/pdfDocuments')
	#script="document.querySelector('body > settings-ui').shadowRoot.querySelector('#main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('#advancedPage > settings-section.expanded > settings-privacy-page').shadowRoot.querySelector('#pages > settings-subpage.iron-selected > settings-pdf-documents').shadowRoot.querySelector('#toggle').shadowRoot.querySelector('#control').shadowRoot.querySelector('button').click()"
	script='document.querySelector("body > settings-ui").shadowRoot.querySelector("#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("#basicPage > settings-section.expanded > settings-privacy-page").shadowRoot.querySelector("#pages > settings-subpage > settings-pdf-documents").shadowRoot.querySelector("#toggle").shadowRoot.querySelector("#control").shadowRoot.querySelector("#knob").click()'
	time.sleep(1)
	driver.execute_script(script)
	time.sleep(1)

def directoryCheck(state):
	npath=path+"/Meghalaya"
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)


def download(driver,divData,ty,fname):
	j=0
	for i in range(len(divData)):
		title=driver.find_element_by_xpath('//*[@id="showoutput"]/table/tbody/tr['+str(i+1)+']/td[3]').text
		if ty.lower() in title.lower():
			driver.find_element_by_xpath('//*[@id="showoutput"]/table/tbody/tr['+str(i+1)+']/td[4]/a').click()
			j=j+1
	time.sleep(3)
	try:
		os.rename(dpath+'/display_causelist.pdf',path+'/Meghalaya/'+fname+' List/'+name+'/list_1.pdf')
	except:
		pass
	for i in range(1,j):
		try:
			os.rename(dpath+'/display_causelist ('+str(i)+').pdf',path+'/Meghalaya/'+fname+' List/'+name+'/list_'+str(i+1)+'.pdf')
		except:
			pass
def extract():
	directoryCheck('Daily List/'+name)
	directoryCheck('Supplementary List/'+name)
	url="https://services.ecourts.gov.in/ecourtindiaHC/cases/highcourt_causelist.php?state_cd=21&dist_cd=1&court_code=1&stateNm=Meghalaya"

	driver=webdriver.Chrome(executable_path=cpath)
	preference(driver)
	driver.get(url)

	data=driver.find_element_by_xpath('//*[@id="causelist_dt"]')
	data.send_keys(date)

	btn=driver.find_element_by_xpath('//*[@id="go"]')
	btn.click()

	htmlPage=driver.page_source
	soup=BeautifulSoup(htmlPage,features="html.parser")
	divData=soup.findAll('a',attrs={'style':'color:#559DE7; font-weight:bold;text-decoration: underline;'})

	download(driver,divData,'DAILY','Daily')
	download(driver,divData,'SUPPLEMENTARY','Supplementary')

def main():
	extract()

if __name__=="__main__":
	main()
