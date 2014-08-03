# -*- coding: utf-8 -*-

# from scrapy.utils.project import get_project_settings
import scrapy
import json
from scrapy.http import Request
from crawler.items import CrawlerItem,CommentItem
from crawler.config.keygen import *
from crawler.config import oauth2
from crawler.utils import jsonselect
from urlparse import urlparse,parse_qs

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
		if kwargs.get('name') != None and kwargs.get('password') != None:
			ProcessAbstract.encryProcess(Encryption(),kwargs.get('name'),kwargs.get('password'))
			exit(0)
		elif os.path.isfile('.pubkey.key')==False:
			ProcessAbstract.encryProcess(Encryption())
			exit(0)

		self.dig_depth = 1
		self.access_token = oauth2.getAccessToken()
		self.username = kwargs.get('name')
		self.allowed_domains = ["weibo.com"]
		self.start_urls = [
			"https://api.weibo.com/2/statuses/user_timeline.json?screen_name=%s&page=%s&count=1&access_token=%s" % (self.username,self.dig_depth,self.access_token)
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
		# print response.encoding
		tojson = json.loads(response.body_as_unicode())
		
		for l in tojson.get('statuses'):
			parser = jsonselect.Parser(l)
			id = parser.parse(':root > .id')
			tweet = parser.parse(':root > .text')
			# retweeted = parser.parse(':root .retweeted_status .text')
			# thumbnail_pic = parser.parse(':root .retweeted_status .pic_urls .thumbnail_pic')

			if id:
				item = CrawlerItem()
				item['id'] = id
				item['tweet'] = tweet
				yield item

				comment_link = "https://api.weibo.com/2/comments/show.json?id=%s&access_token=%s" % (id,self.access_token)
				yield Request(url=comment_link, callback=self.comment_parse)

				# self.dig_depth += 1
				# next_link = "https://api.weibo.com/2/statuses/user_timeline.json?screen_name=%s&page=%s&access_token=%s" % (self.username,self.dig_depth,self.access_token)
				# yield Request(url=next_link, callback=self.parse)
		# return items



	def comment_parse(self,response):
		items = []
		tojson = json.loads(response.body_as_unicode())
		for l in tojson.get('comments'):
			parser = jsonselect.Parser(l)
			comment = parser.parse(':root > .text')
			if comment:
				item = CommentItem()
				item['comment'] = comment
				item['id'] = parse_qs(urlparse(response.url).query)['id']
				# yield item
				items.append(item)
		return items


















