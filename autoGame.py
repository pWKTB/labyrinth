# coding: utf-8
import ConfigParser
import platform
import time
import urllib
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

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
		self.driver.set_window_size(400,1000)

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

#	def pressTab(self,n):
#		keyboard = self.driver.find_element_by_xpath("/html")
#		for i in xrange(1,n):
#			keyboard.send_keys(Keys.TAB)
#		#keyboard.send_keys(Keys.ENTER)

	def splitQuestUrl(self,url):
		decode_url = urllib.unquote(url)
		split_url = decode_url.split("/hkt48/")
		result_url = split_url[1].split("?")
		return result_url[0]

	#ログイン
	def login(self):
		self.driver.get(self.login_url);
		loginboxes = [tag for tag in self.driver.find_elements_by_tag_name('input')]
		loginboxes[0].send_keys(self.mailaddress)
		loginboxes[1].send_keys(self.password)
		loginboxes[2].send_keys(Keys.RETURN)

	#エンター
	def enter(self):
		time.sleep(1)
		self.click("img","src","http://img.isky.am/img/sp/img/alert_message.png",1)
		self.driver.execute_script('window.scrollBy(0,700)')
		self.click("h3","text","HKT",0)

	def startAdventure(self):
		self.click("a","title","MENU",1)
		self.click("area","title",u"冒険",1)

	def visiblePainted(self):
		#self.driver.execute_script("var div_element = document.createElement('div');div_element.setAttribute('style', 'position: absolute; left: 100px; top: 380px;　width:10px;　height:10px; background-color:white;');div_element.setAttribute('id', 'test');var parent_object = document.getElementById('swiffycontainer');parent_object.appendChild(div_element);")
		time.sleep(10)
		#self.click("div","id","test",1)
		#self.click("div","xpath",'//*[@id="swiffycontainer"]/div[1]/svg/g/g/g/g/g[1]/g[1]/g/path',1)
		webdriver = self.driver
		target = webdriver.find_element_by_id("swiffycontainer")
		#ActionChains(self.driver).move_to_element(target).move_by_offset(100,380).click()
        action = ActionChains(webdriver)
        action.perform()
        #action.move_by_offset(100,380).click()
        #action.move_to_element(target)
		#print action
        #action.move_by_offset(100,380)
        #actions.click()


	def venture(self):
		while 1:
			url = self.driver.current_url
			current = self.splitQuestUrl(url)
			print current

			if current == "quest/index":
				btn = [tag for tag in self.driver.find_elements_by_tag_name('a')]
				if u"ボス戦へ挑む" in btn[0].text:
					self.click("a","class","btnType_red liquid",1)
				else :
					self.click("a","text",u"冒険",0)
			elif current == "top/index":
				self.click("a","class","myButton",1)
			elif current == "mypage/index":
				self.startAdventure()
			elif current == "quest/questResult":
				btn = [tag for tag in self.driver.find_elements_by_tag_name('a')]
				if u"ボス戦へ挑む" in btn[0].text:
					self.click("a","class","btnType_red liquid",1)
				else :
					self.click("a","text",u"冒険",0)
			elif current == "quest/scenario/logic":
				self.click("div","xpath","/html/body/div/div",1)
			elif current == "quest/itemDropResult":
				self.click("a","text",u"次へ",1)
			elif current == "quest/bossIndex":
				self.click("a","class","btnType_red liquid",1)

			elif current == "quest/bossSwf":
				self.visiblePainted()
				break

			elif current == "quest/bossWinResult":
				self.click("a","class","btnType_gray_radius",1)
			elif current == "quest/actionEmpty":
				for m in xrange(0,10):
					for s in xrange(0,6):
						print str(m) + ":" + str(s*10)
						time.sleep(10)
				self.startAdventure()
			#elif
			else :
				self.click("div","xpath","/html/body/div/div",1)

if __name__ == '__main__':
	ag = AutoGame()
	ag.action()