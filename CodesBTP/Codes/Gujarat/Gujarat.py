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
def preference(driver):
	driver.get('chrome://settings/content/pdfDocuments')
	#script="document.querySelector('body > settings-ui').shadowRoot.querySelector('#main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('#advancedPage > settings-section.expanded > settings-privacy-page').shadowRoot.querySelector('#pages > settings-subpage.iron-selected > settings-pdf-documents').shadowRoot.querySelector('#toggle').shadowRoot.querySelector('#control').shadowRoot.querySelector('button').click()"
	script='document.querySelector("body > settings-ui").shadowRoot.querySelector("#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("#basicPage > settings-section.expanded > settings-privacy-page").shadowRoot.querySelector("#pages > settings-subpage > settings-pdf-documents").shadowRoot.querySelector("#toggle").shadowRoot.querySelector("#control").shadowRoot.querySelector("#knob").click()'
	time.sleep(1)
	driver.execute_script(script)
	time.sleep(1)

def directoryCheck(state):
	#path="/home/sailok/Desktop/BTP Data"
	fpath=path+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(path+'/'+state)

def extract():
	directoryCheck('Gujarat')
	url="http://gujarathc-casestatus.nic.in/gujarathc/"

	driver=webdriver.Chrome(executable_path='C:/Users/Sritej. N/Downloads/chromedriver_win32/chromedriver')
	preference(driver)
	driver.get(url)

	time.sleep(1)
	data=driver.find_element_by_xpath('//*[@id="divinclude"]/div[2]/div[2]/div[6]/a')
	data.click()

	time.sleep(1)
	data2=driver.find_element_by_xpath('//*[@id="gobutton"]')
	data2.click()

	time.sleep(1)
	btn=driver.find_element_by_xpath('//*[@id="divbtn"]/div[1]/div/button[5]')
	btn.click()

	time.sleep(1)
	btn2=driver.find_element_by_xpath('//*[@id="getlist"]')
	btn2.click()

	time.sleep(5)

	os.rename(dpath+'/clist_'+date.replace('-','_')+'.pdf',path+'/Gujarat/'+name+'.pdf')
def main():
	extract()

if __name__=="__main__":
	main()
