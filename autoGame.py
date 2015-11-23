# coding: utf-8
import ConfigParser
import platform
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class AutoGame(object):
	mailaddress = ""
	password = ""
	chromedriver_path = ""
	deviceName = ""
	login_url = ""
	driver = "" #webdriverの入るグローバル変数

	def __init__(self):
		self.initConfig()
		self.initChromedriverPath()
		self.initDriver()

	def action(self):
		self.login()
		self.enter()
		self.venture()

	#設定ファイルからの読み込み
	def initConfig(self):
		inifile = ConfigParser.SafeConfigParser()
		inifile.read("./config.ini")
		self.mailaddress = inifile.get("account","mailaddress")
		self.password = inifile.get("account","password")
		self.deviceName = inifile.get("system","deviceName")
		self.login_url = inifile.get("url","login")

	#Chrome diriverのパス設定
	def initChromedriverPath(self):
		os = platform.system()
		#Chrome diriverのパス
		if os == "Windows":
			self.chromedriver_path = "./chrom/chromedriver.exe"
		else :
			self.chromedriver_path = "./chrom_mac/chromedriver"

	#webDriverの初期設定
	def initDriver(self):
		chromeOptions = webdriver.ChromeOptions()
		mobile_emulation = {"deviceName" : self.deviceName}
		chromeOptions.add_experimental_option("mobileEmulation",mobile_emulation)
		self.driver = webdriver.Chrome(executable_path=self.chromedriver_path, chrome_options=chromeOptions)
		self.driver.set_window_size(400,500)

	def click(self,tag,attribute,content,match):
		if attribute == "xpath":
			self.clickXpath(content)
		else :
			self.clickTagSearch(tag,attribute,content,match)

	#クリック関数(タグの要素名,タグ内の属性名,タグ内の属性値,完全一致なら1)
	def clickTagSearch(self,tag,attribute,content,match):
		if match:
			if attribute == "text":
				while 1:
					print "search"
					tags = [tag for tag in self.driver.find_elements_by_tag_name(tag) if tag.text == content]
					if len(tags) != 0:
						break
			else :
				while 1:
					print "search"
					tags = [tag for tag in self.driver.find_elements_by_tag_name(tag) if tag.get_attribute(attribute) == content]
					if len(tags) != 0:
						break					
		else :
			if attribute == "text":
				while 1:
					print "search"
					tags = [tag for tag in self.driver.find_elements_by_tag_name(tag) if content in tag.text]
					if len(tags) != 0:
						break
			else :
				while 1:
					print "search"
					tags = [tag for tag in self.driver.find_elements_by_tag_name(tag) if content in tag.get_attribute(attribute)]
					if len(tags) != 0:
						break
		tags[0].click()
		print "click"

	def clickXpath(self,path):
		time.sleep(1)
		tag = self.driver.find_element_by_xpath(path)
		pre_id = tag.id
		while 1:
			if tag.id != pre_id:
				break
			else :
				tag.click()
				pre_id = tag.id
				print "touch"
				print pre_id
				print tag.id
				time.sleep(1)
				tag = self.driver.find_element_by_xpath(path)

	#ログイン
	def login(self):
		self.driver.get(self.login_url);
		loginboxes = [tag for tag in self.driver.find_elements_by_tag_name('input')]
		loginboxes[0].send_keys(self.mailaddress)
		loginboxes[1].send_keys(self.password)
		loginboxes[2].send_keys(Keys.RETURN)

	#エンター
	def enter(self):
		self.click("img","src","http://img.isky.am/img/sp/img/alert_message.png",1)
		self.driver.execute_script('window.scrollBy(0,700)')
		self.click("h3","text","HKT",0)
		self.click("a","class","myButton",1)

	def startAdventure(self):
		self.click("a","title","MENU",1)
		self.click("area","title",u"冒険",1)

	def venture(self):
		self.startAdventure()
		self.click("a","class","btnType_new",1)
		self.click("div","xpath","/html/body/div/div",1)
		self.click("div","xpath","/html/body/div/div",1)
		self.click("a","text",u"次へ",1)

if __name__ == '__main__':
	ag = AutoGame()
	ag.action()