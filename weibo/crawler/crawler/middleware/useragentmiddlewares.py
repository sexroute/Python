# -*- coding: utf-8 -*-

import random
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class SwitchUserAgentMiddleware(UserAgentMiddleware):
	user_agent_list = [
		'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
		'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
		'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17'
	]

	def __init__(self, user_agent=''):
		self.user_agent = user_agent

	def _user_agent(self, spider):
		if hasattr(spider, 'user_agent'):
			return spider.user_agent
		elif self.user_agent:
			return self.user_agent
		return random.choice(self.user_agent_list)

	def process_request(self, request, spider):
		ua = self._user_agent(spider)
		if ua:
			request.headers.setdefault('User-Agent', ua)

	def function(self,request,response,spider):
		print request.headers
		return response
