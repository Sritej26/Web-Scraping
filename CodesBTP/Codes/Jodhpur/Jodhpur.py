import datetime
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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
	npath=path+"/Jodhpur"
	fpath=npath+'/'+state
	if os.path.exists(fpath):
		pass
	else:
		os.mkdir(npath+'/'+state)

def exist_alert(driver):
	try:
		driver.find_element_by_xpath('//*[@id="showModelForAllTypes"]/div[2]')
	except NoSuchElementException:
		return False
	return True

def rename(date,ty):
	for fname in os.listdir(dpath):
		if "SearchCauselist" in fname:
			os.rename(dpath+'/'+fname,path+'/Jodhpur/'+ty+'/'+name+'.html')
			break

def download(url,date,driver,i):
	dateForm=driver.find_element_by_xpath('//*[@id="causelstdt"]')
	dateForm.clear()
	dateForm.send_keys(date)
	dateForm.send_keys(u'\ue007')

	driver.find_element_by_xpath('//*[@id="causelisttype"]/option['+str(2+i)+']').click()
	time.sleep(2)

	if exist_alert(driver):
	 	driver.find_element_by_xpath('//*[@id="showModelForAllTypes"]/div[2]/div/form/div[2]/div[2]/div/button').click()
	 	print "NO:"+date
	else:
		try:
			driver.find_element_by_xpath('//*[@id="btnSearchCauseList"]').click()
			time.sleep(4)
		except:
			print "NO:"+date
			pass


def main():
	url="https://hcraj.nic.in/cishcraj-jdp/causelists/"
	#chrome_options = webdriver.ChromeOptions()
	#chrome_options.add_argument("--headless")
	driver=webdriver.Chrome(executable_path=cpath)#,chrome_options=chrome_options)
	driver.get(url)
	#driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
	#params = {'cmd': 'Page.setDownloadBehavior'}
	#command_result = driver.execute("send_command", params)

	x=['Daily','Supplementary','Weekly','Regular']
	j=0
	for y in x:
		directoryCheck(y)
		download(url,date,driver,j)
		j+=1
		rename(date.replace('-','/'),y)

if __name__ == '__main__':
	main()
