import urllib2
import datetime
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def directoryCheck(state):
	npath=path+"/Shimla"		
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)

def supplementary(url):
	driver=webdriver.Chrome(executable_path=cpath)	
	driver.get(url)

	#driver.switch_to_alert().accept()

	select=driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/select')
	size=len(select.find_elements_by_tag_name("option"))

	for i in range(1,size+1):
		opt=driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/select/option['+str(i)+']')
		if opt.text==date:
			opt.click()
			break

	driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[2]/input').click()
	driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[3]/td/table/tbody/tr/td[3]/input').click()
	driver.execute_script('return document.getElementsByClassName("btnclass")[1]').click()
	
	driver.switch_to_alert().accept()
	webPage=driver.page_source
				
	with open(path+'/Shimla/Supplementary List/'+name+'.html','wb') as f:
				f.write(webPage.encode('utf-8'))
def dailyList(url):
	driver=webdriver.Chrome(executable_path=cpath)	
	#driver=webdriver.Firefox(executable_path='/home/sailok/Downloads/geckodriver-v0.24.0-linux64/geckodriver')	
	driver.get(url)

	#driver.switch_to_alert().accept()

	select=driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/select')
	size=len(select.find_elements_by_tag_name("option"))

	for i in range(1,size+1):
		opt=driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[3]/td/table/tbody/tr/td[2]/select/option['+str(i)+']')
		if opt.text==date:
			opt.click()
			break

	driver.find_element_by_xpath('/html/body/form/table[3]/tbody/tr[3]/td/table/tbody/tr/td[3]/input').click()

	driver.execute_script('return document.getElementsByClassName("btnclass")[1]').click()

	driver.switch_to_alert().accept()
	webPage=driver.page_source
				
	with open(path+'/Shimla/Daily List/'+name+'.html','wb') as f:
				f.write(webPage.encode('utf-8'))
	
def main():
	url="https://highcourt.hp.gov.in/cmis/websitephps1/netbd.php"
	dailyList(url)
	supplementary(url)

if __name__=="__main__":
	main()
