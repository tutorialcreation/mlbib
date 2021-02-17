# downloading the web page

import urllib2
import urlparse


class Throttle:
	def __init__(self,delay):		
		self.delay=delay
		self.domains={}

	def wait(self,url):
		domain=urlparse.urlparse(url).netloc
		last_accessed=self.domains.get(domain)
		
		if self.delay > 0 and last_accessed is not None:
			sleep_secs=self.delay-(datetime.datetime.now()-last_accessed).seconds
			if sleep_secs > 0:
				time.sleep(sleep_secs)
		self.domains[domain]=datetime.datetime.now()












def download(url,user_agent='wswp',num_retries=2,proxy=None):
	print("Downloading: ",url)
	headers={'User-agent':user_agent}
	request=urllib2.Request(url,headers=headers)
	opener=urllib2.build_opener()
	if proxy:
		proxy_params={urlparse.urlparse(url).scheme:proxy}
		opener.add_handler(urllib2.ProxyHandler(proxy_params))
	try:
		html=urllib2.urlopen(url).read()
	except urllib2.URLError as e:
		print("Download error: ",e.reason)
		html=None
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download(url,num_retries-1)
	return html
