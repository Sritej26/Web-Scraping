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
	directoryCheck('Andhra/'+name)
	url="http://hc.ap.nic.in/Hcdbs/search.do"

	driver=webdriver.Chrome(executable_path='C:/Users/Sritej. N/Downloads/chromedriver_win32/chromedriver')
	preference(driver)
	driver.get(url)

	time.sleep(1)
	data=driver.find_element_by_xpath('//*[@id="content"]/div[1]/div/input[1]')
	data.click()

	time.sleep(1)
	data2=driver.find_element_by_xpath('//*[@id="content"]/div/input[1]')
	data2.click()

	time.sleep(1)
	select=driver.find_element_by_xpath('//*[@id="court"]')
	time.sleep(1)
	size=len(select.find_elements_by_tag_name("option"))
	for i in range(2,size+1):
		opt=driver.find_element_by_xpath('//*[@id="court"]/option['+str(i)+']')
		fname=opt.text.replace(' ','_')
		opt.click()
		time.sleep(7)
		with open(path+'/Andhra/'+name+'/'+fname+'.html','wb') as f:
					f.write(driver.page_source.encode("utf-8"))
		driver.back()
def main():
	extract()

if __name__=="__main__":
	main()
