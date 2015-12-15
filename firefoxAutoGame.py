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
	deviceName = ""
	login_url = ""
	driver = "" #webdriverの入るグローバル変数
	flg_break = 0

	def __init__(self):
		self.initConfig()
		self.initDriver()

	def action(self):
		self.login()
		self.enter()
		#self.autoQuest()
		self.autoEvent()

	#設定ファイルからの読み込み
	def initConfig(self):
		inifile = ConfigParser.SafeConfigParser()
		inifile.read("./config.ini")
		self.mailaddress = "tnk-snow-mind1209@ezweb.ne.jp"
		self.password = "keyof75321"
		self.deviceName = "Apple iPhone 6"
		self.login_url = "http://sp.isky.am/login.php"

	#webDriverの初期設定
	def initDriver(self):
		profile = webdriver.FirefoxProfile()
		profile.set_preference("general.useragent.override","Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3")
		self.driver = webdriver.Firefox(profile)
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

	def clickCoordinate(self,offset_x,offset_y):
		time.sleep(5)
		ActionChains(self.driver).move_by_offset(offset_x,offset_y).click().perform()
		ActionChains(self.driver).move_by_offset(-(offset_x),-(offset_y)).perform()


	def splitQuestUrl(self,url):
		decode_url = urllib.unquote(url)
		split_url = decode_url.split("/hkt48/")
		result_url = split_url[1].split("?")
		return result_url[0].split("/")

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

	def startQuest(self):
		self.click("a","title","MENU",1)
		self.click("area","title",u"冒険",1)

	def autoQuest(self):
		while 1:
			url = self.driver.current_url
			current = self.splitQuestUrl(url)
			print current[0] + current[1]
			if current[0] == "top":
				self.top(current[1])
			elif current[0] == "mypage":
				self.mypage(current[1])
			elif current[0] == "quest":
				self.quest(current[1])
			else :
				self.click("div","xpath","/html/body/div/div",1)
			if self.flg_break:
				self.driver.close()
				break

	def top(self,path):
		if path == "index":
			btn = [tag for tag in self.driver.find_elements_by_tag_name('a')]
			if u"メンテナンス終了を確認する" in btn[0].text:
				self.driver.close()
				self.flg_break = 1
			else :
				self.click("a","class","myButton",1)
		else :
			self.click("div","xpath","/html/body/div/div",1)

	def mypage(self,path):
		if path == "index":
			self.startQuest()
		else :
			self.click("div","xpath","/html/body/div/div",1)

	def quest(self,path):
		if path == "index" or path == "questResult":
			btn = [tag for tag in self.driver.find_elements_by_tag_name('a')]
			if u"ボス戦へ挑む" in btn[0].text:
				self.click("a","class","btnType_red liquid",1)
			else :
				self.click("a","text",u"冒険",0)
		elif path == "itemDropResult":
			self.click("a","text",u"次へ",1)
		elif path == "bossIndex":
			self.click("a","class","btnType_red liquid",1)
		elif path == "bossSwf":
			self.clickCoordinate(100,380)
		elif path == "bossWinResult":#バグかも
			self.click("a","class","btnType_gray_radius",1)
		elif path == "actionEmpty":
			self.flg_break = 1
		else :
			self.click("div","xpath","/html/body/div/div",1)

	def autoEvent(self):
		while 1:
			url = self.driver.current_url
			current = self.splitQuestUrl(url)
			print current[0] + current[1]
			if current[0] == "top":
				self.top(current[1])
			elif current[0] == "mypage":
				self.mypageEvent(current[1])
			elif current[0] == "event036Raid":
				self.event036Raid(current[1])
			else :
				self.click("div","xpath","/html/body/div/div",1)
			if self.flg_break:
				self.driver.close()
				break

	def mypageEvent(self,path):
		if path == "index":
			self.click("a","class","none btnType_flash",1)
		else :
			self.click("div","xpath","/html/body/div/div",1)

	def event036Raid(self,path):
		if path == "index" or path == "questResult":
			self.click("img","src","latest_quest.png",0)
		elif path == "questInfo" or path == "itemDropResult" or path == "bossWinResult":
			self.click("a","text",u"探索する",1)
		elif path == "itemDropResult":
			self.click("div","xpath","/html/body/div/div",1)
		elif path == "bossIndex":
			tag = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[6]/div/table/tbody/tr[2]/td/div[2]")
			#/html/body/div/div[2]/div[6]/div/table/tbody/tr[2]/td/div[3]/div
			status = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[3]")
			status_split = status.text.split(" ")
			hp =status_split[1]
			#btn = [tag for tag in self.driver.find_elements_by_tag_name('div')  if tag.get_attribute("style") == "color:#FF0000;"]
			print tag.text[4:5] + " : " + hp
			if tag.text == u"BPが足りない！":
				self.flg_break = 1
			else :
				#if self.bossFlg(tag.text[4:5],hp):
				self.click("input","type","submit",1)
				#else :
				#	self.click("a","text",u"エリアに戻る",1)
		elif path == "actionEmpty":
			self.flg_break = 1
		elif path == "loginBonusResult":
			self.click("a","text",u"イベントTOPへ",1)
		else :
			self.click("div","xpath","/html/body/div/div",1)

	def bossFlg(self,bp,hp):
		if hp < (bp * 57729):
			return 1
		else :
			return 0

if __name__ == '__main__':
	ag = AutoGame()
	ag.action()