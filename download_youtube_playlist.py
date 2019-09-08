import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
driver = webdriver.Firefox(options = options, executable_path=r"geckodriver.exe")
og_win = driver.window_handles[0]

a=[]
driver.get("")   #Enter the Keepvid.pro/youtube-playlist link
time.sleep(10)
link = driver.find_elements_by_tag_name('a')
for l in link:
	url = str(l.get_attribute('href'))
	if 'redirector.googlevideo.com' in url:
		a.append(url)

driver.execute_script('window.open("'+a[0]+'","_blank")')
time.sleep(5)
for i in a[1:]:
	driver.execute_script('window.open("'+i+'","_blank")')
	time.sleep(4)
