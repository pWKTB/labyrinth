# coding: utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

chromeOptions = webdriver.ChromeOptions()
mobile_emulation = {"deviceName" : "Apple iPhone 6"}
chromeOptions.add_experimental_option("mobileEmulation",mobile_emulation)
#Chrome diriverのパス
chromedriver = "./chrom/chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

login_url = 'http://sp.isky.am/login.php'
driver.get(login_url);

loginboxes = [tag for tag in driver.find_elements_by_tag_name('input')]
mailaddress = loginboxes[0]
password = loginboxes[1]

mailaddress.send_keys('tnk-snow-mind1209@ezweb.ne.jp')
password.send_keys('keyof75321')

submit = loginboxes[2]
submit.send_keys(Keys.RETURN)


#try:
#    element = WebDriverWait(driver, 10).until(
#    	[tag for tag in driver.find_elements_by_tag_name('h3') if u'HKT48' in tag.text]
#    	)
#    print ("OK, page loaded")
#except:
#    print ("Loading took too much time!")



#####
while 1:
	links = [tag for tag in driver.find_elements_by_tag_name('h3') if u'HKT48' in tag.text]
	print links[0].text
	if links[0] is not None:
		alertMessages = [tag for tag in driver.find_elements_by_tag_name('img') if tag.get_attribute('src') == 'http://img.isky.am/img/sp/img/alert_message.png']
		if alertMessages[0] is not None:
			alertMessages[0].click()
		time.sleep(1)
		links[0].click()
		break

#####
menu = [tag for tag in driver.find_elements_by_tag_name('a') if tag.get_attribute('title') == u'MENU']
menu[0].click()

jobs = [tag for tag in driver.find_elements_by_tag_name('area') if tag.get_attribute('title') == u'冒険']
jobs[0].click()

#####
works = [tag for tag in driver.find_elements_by_tag_name('a') if tag.get_attribute('class') == 'btnType_new']
print works[0].get_attribute('class')
works[0].click()

#####
#pushs = [tag for tag in driver.find_elements_by_tag_name('path')]
#for push in pushs:
#	print push.get_attribute("fill")
#pushs[0].click()

time.sleep(1)
push = driver.find_element_by_xpath('/html/body/div/div')
push.click()

time.sleep(1)
push.click()

time.sleep(1)
push = driver.find_element_by_xpath('/html/body/div/div')
push.click()

#while 1:
#push = driver.find_element_by_xpath('/html/body/div/div/div/svg/g/g/g/g/g[7]')
#	#print push.get_attribute('transform')
#	if push is not None:
#	
#push.click()
#		break

#driver.execute_script("")