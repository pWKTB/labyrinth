# coding: utf-8
from firefoxAutoGame import *

class AutoGameEvent042Raid(AutoGame):
    #def __init__(self):
    #    AutoGame.__init__(self)

	def action(self):
		self.login()
		self.enter()
		self.autoEvent()

	#アカウントの設定
	def initAcount(self):
		#self.mailaddress = "tnk-snow-mind1209@ezweb.ne.jp"
		#self.mailaddress = "tayukinatu88-7135@ezweb.ne.jp"
		#self.mailaddress = "metayas17@ezweb.ne.jp"
		self.mailaddress = "natuyu12638@ezweb.ne.jp"
		self.password = "keyof75321"

	def autoEvent(self):
		while 1:
			url = self.driver.current_url
			current = self.splitQuestUrl(url)
			print current[0] + current[1]
			if current[0] == "top":
				self.top(current[1])
			elif current[0] == "mypage":
				self.mypageEvent(current[1])
			elif current[0] == "event042Raid":
				self.event042Raid(current[1])
			else :
				self.click("div","xpath","/html/body/div/div",1)
			if self.flg_break:
				self.driver.close()
				break

	def event042Raid(self,path):
		if path == "index" or path == "questResult":
			#self.click("a","text",u"最新のクエスト",0)
			self.searchBoss()
			#self.click("img","src","http://lb-hkt48-web-2006873409.ap-northeast-1.elb.amazonaws.com/hkt48/images/sp/event/039Raid/area/7.png",1)
		elif path == "questInfo" or path == "itemDropResult" or path == "bossWinResult" or path == "bossLoseResult" or path == "eventEncountResult":
			bps = [tag for tag in self.driver.find_elements_by_tag_name('img')  if tag.get_attribute("src") == "http://lb-hkt48-web-2006873409.ap-northeast-1.elb.amazonaws.com/hkt48/images/sp/common/bar/bp_0.png"]
			print len(bps)
			if len(bps) == 1:
				self.flg_break = 1
			else :
				self.click("a","text",u"探索する",1)
		elif path == "itemDropResult":
			self.click("div","xpath","/html/body/div/div",1)
		elif path == "bossIndex" or path == "bossIndex#undefined":
			#status = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]")
			#level = re.search(u"【Lv.(.*?)】", status.text).group(1)
			status = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[3]")
			level = re.search(u"HP: (.*?) /", status.text).group(1)
			print level

			#/html/body/div/div[2]/div[4]/div[2]/img
			img = [tag for tag in self.driver.find_elements_by_tag_name('img')]
			src = img[25].get_attribute("src")
			bp = src[-8:]
			print bp
			#status_split = status.text.split(" ")
			#hp =status_split[1]
			#btn = [tag for tag in self.driver.find_elements_by_tag_name('div')  if tag.get_attribute("style") == "color:#FF0000;"]
			#level = self.driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]")
			#status = img[5].get_attribute("src")
			if bp == "acer.gif":
				self.flg_break = 1
			else :
				if self.bossFlg(level,bp):
					self.click("input","type","submit",1)
				else :
					self.click("a","text",u"エリアに戻る",1)
		elif path == "quintetResult":
			self.click("a","text",u"探索",1)
		elif path == "questClear" or path == "itemDrop":
			self.click("a","text","SKIP",1)
		elif path == "bossSwf":
			self.clickCoordinate(100,380)
		elif path == "cardLevelUp":
			self.clickCoordinate(200,350)
		elif path == "LevelUp":
			self.clickCoordinate(100,380)
		elif path == "actionEmpty":
			self.flg_break = 1
		elif path == "eventEncountSelectAction":
			self.click("a","text",u"プレゼント小",1)
		elif path == "loginBonusResult":
			self.click("a","text",u"イベントTOPへ",1)
		else :
			self.click("div","xpath","/html/body/div/div",1)

	def bossFlg(self,tag,tag_sub):
		d = datetime.datetime.today()
		date = '%s ' % d
		data = tag + " " + date + "\n"
		print data
		f = open('C:\User_Program\labyrinth\level.txt', 'a+') # 書き込みモードで開く
		f.write(data) # 引数の文字列をファイルに書き込む
		f.close() # ファイルを閉じる

		hp = tag
		bp = re.search(u"bp_(.*?).png", tag_sub).group(1)

		print "HP = " + hp + "  BP = " + bp + "  MAX AP = " + str((int(bp)+4)*161545)
		if int(hp) < ((int(bp)+3)*100000):
		#if 1:
			return 1
		else :
			return 0

	def searchBoss(self):
		img = [tag for tag in self.driver.find_elements_by_tag_name('img')]
		src = img[1].get_attribute("src")
		quest_flg = 1
		print src
		if src != "http://lb-hkt48-web-2006873409.ap-northeast-1.elb.amazonaws.com/hkt48/images/sp/event/042Raid/base/appear.png":
			self.click("img","src","http://lb-hkt48-web-2006873409.ap-northeast-1.elb.amazonaws.com/hkt48/images/sp/event/042Raid/area/1.png",1)
		else :
			self.click("img","src","http://lb-hkt48-web-2006873409.ap-northeast-1.elb.amazonaws.com/hkt48/images/sp/event/042Raid/base/appear.png",1)
			divs = [tag for tag in self.driver.find_elements_by_tag_name('div')  if tag.get_attribute("class") == "eventBtnPopUp"]
			print len(divs)
			for x in xrange(1,len(divs)+1):
				xpath = '//*[@id="appear"]/div[2]/div[' + str(x+1) +']/table/tbody/tr/td[2]/div[1]'
				boss = self.driver.find_element_by_xpath(xpath)
				#print boss.text
				hp = re.search(u"HP (.*?)/", boss.text).group(1)
				mhp = re.search(u"/(.*?)\n", boss.text).group(1)
				print hp + "/" + mhp
				print mhp
				if int(hp) < int(mhp):
					divs[x-1].click()
					print "quest"
					quest_flg = 0
					break
			if quest_flg:
				self.click("img","src","http://lb-hkt48-web-2006873409.ap-northeast-1.elb.amazonaws.com/hkt48/images/sp/event/042Raid/area/1.png",1)


if __name__ == '__main__':
	ag = AutoGameEvent042Raid()
	ag.action()