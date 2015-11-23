# coding: utf-8
from selenium import webdriver
import time
import platform
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

chromeOptions = webdriver.ChromeOptions()
mobile_emulation = {"deviceName" : "Apple iPhone 6"}
chromeOptions.add_experimental_option("mobileEmulation",mobile_emulation)

os = platform.system()
#Chrome diriverのパス
if os == "Windows":
	chromedriver = "./chrom/chromedriver.exe"
else :
	chromedriver = "./chrom_mac/chromedriver"

#Chrome diriverのパス
chromedriver = "./chrom_mac/chromedriver"

driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

login_url = 'http://sp.isky.am/login.php'
driver.get(login_url);

