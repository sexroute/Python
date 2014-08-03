# -*- coding: utf-8 -*-

# from scrapy.utils.project import get_project_settings
import scrapy
import json
from scrapy.http import Request
from crawler.items import CrawlerItem
from crawler.config.keygen import *
from crawler.config import oauth2
from crawler.utils import jsonselect
from pprint import pprint

from urlparse import urljoin
clean_url = lambda base_url,u,response_encoding: urljoin(base_url, remove_entities(clean_link(u.decode(response_encoding))))


class WbSpider(scrapy.Spider):
	name = "Weibo"
	
	# start_urls = [
		# "http://192.168.1.108:8080/json/index.json"
		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
  		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        # "https://api.weibo.com/2/statuses/user_timeline.json?screen_name=%s&page=%s&access_token=%s" % (kwargs.get('name'),1,oauth2.getAccessToken())
        # "http://scrapy.org"
        # "https://api.weibo.com/2/statuses/user_timeline.json?screen_name=-Luxe&page=1&access_token=2.00XIqViCoblvpD87e9d1d4850Dtyjx"
	# ]

	def __init__(self, category=None, *args, **kwargs):
		super(WbSpider, self).__init__(*args, **kwargs)
		# print kwargs
		# print kwargs.get('name')
		if kwargs.get('name') != None and kwargs.get('password') != None:
			ProcessAbstract.encryProcess(Encryption(),kwargs.get('name'),kwargs.get('password'))
			exit(0)
		elif os.path.isfile('.pubkey.key')==False:
			ProcessAbstract.encryProcess(Encryption())
			exit(0)

		self.allowed_domains = ["weibo.com"]
		self.start_urls = [
			"https://api.weibo.com/2/statuses/user_timeline.json?screen_name=%s&page=%s&access_token=%s" % (kwargs.get('name'),1,oauth2.getAccessToken())
			# "http://www.woaidu.org/sitemap_1.html"
		]

	def parse(self, response):
		# filename = response.url.split("/")[-2]
		# with open(filename,'wb') as f:
		# 	f.write(response.body)

		# for sel in response.xpath('//ul/li'):
		# 	titile = sel.xpath('a/text()').extract()
		# 	link = sel.xpath('a/@href').extract()
		# 	desc = sel.xpath('text()').extract()
		# 	print titile,link,desc

		# settings = get_project_settings()
		# print "Your USER_AGENT is:\n%s" % (settings.get('ITEM_PIPELINES'))

		# items = []
		# for sel in response.xpath('//ul/li'):
		# 	item = DmozItem()
		# 	item['titile'] = sel.xpath('a/text()').extract()
		# 	item['link'] = sel.xpath('a/@href').extract()
		# 	item['desc'] = sel.xpath('text()').extract()
			# yield item
		# 	print '--------------------------parse-----------------------------------'
		# 	print item
			# items.append(item)
		# return items

		# print response.body
		# item = CrawlerItem()
		# item['titile'] = 'crawl titile'
		# item['link'] = 'crawl link'
		# item['desc'] = 'crawl desc'
		# yield item
		# print response.body

		# print response.encoding

		# dumjson = json.dumps(text)
		# print dumjson
		tojson = json.loads(response.body_as_unicode())
		# print tojson
		# print tojson['statuses'][0]['id']
		# print tojson['statuses'][0]['text']
		# print tojson['statuses'][0]['retweeted_status']['text']
		
		for l in tojson['statuses']:
			parser = jsonselect.Parser(l)
			id = parser.parse(':root > .id')
			text = parser.parse(':root > .text')
			retweeted = parser.parse(':root .retweeted_status .text')
			thumbnail_pic = parser.parse(':root .retweeted_status .pic_urls .thumbnail_pic')
			print id
			print text
			print retweeted
			print thumbnail_pic
			

		# print tojson['statuses'][0]
		# tojson = json.loads(response.body)
		# print tojson














