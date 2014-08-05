# -*- coding: utf-8 -*-
import base64
import random

class ProxyMiddleware(object):
	proxy_list = [
		'http://192.168.1.124:8088',
		'http://192.168.1.120:8088',
		'http://192.168.1.121:8088',
		'http://192.168.1.123:8088',
		'http://192.168.1.125:8088',
		'http://192.168.1.126:8088',
		'http://192.168.1.127:8088'
	]
	switch = False
	def process_request(self,request,spider):
		proxy = ''
		if self.switch:
			proxy = random.choice(self.proxy_list)
		request.meta['proxy'] = proxy
		# proxy_user_pass = 'name:password'
		# encoded_user_pass = base64.encodestring(proxy_user_pass)
		# request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

	def process_response(self,request,response,spider):
		# print response.status
		# if response.status != 200:
		# 	self.switch = True
		self.switch = True
		print request.meta.get('proxy')
		# print response
		return response
