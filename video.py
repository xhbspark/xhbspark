#-*- coding:UTF-8 -*-
import requests,re, json
from bs4 import BeautifulSoup

class video_dowmloader():
	def __init__(self,url):
		self.server = 'http://api.xfsub.com'
		self.api = 'http://api.xfsub.com/xfsub_api/?url='
		self.get_url_api = 'http://api.xfsub.com/xfsub_api/url.php'
		self.url = url.split('#')[0]
		self.target = self.api + self.url
		self.s = requests.session()
	"""
	:get 'key,time,url'
	Parameters:
	none
	Returns:
	none
	Modif:
	2017-10-18
	"""
	def get_key(self):
		data = {'time':self.info['time'],
		     'key':self.info['key'],
		     'url':self.info['url'],
		     'type':''}
		req = self.s.post(url=self.get_url_api,data=data)
		url = self.server + json.loads(req.text)['rul']
		bf = BeautifulSoup(req.text,'xml')
		video_url = bf.find('file').string
		return video_url
	if __name__ =='__main__':
		url = 'http://www.iqiyi.com/v_19rr7qhfg0.html#vfrm=19-9-0-1'
		vd = video_downloader(url)
		vd.get_key()
		print(vd.get_url)












