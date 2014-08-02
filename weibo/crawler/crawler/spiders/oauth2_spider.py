# -*- coding: utf-8 -*-

import scrapy
from crawler.items import CrawlerItem

from scrapy.utils.project import get_project_settings


class WbSpider(scrapy.Spider):
	name = "Weibo"
	allowed_domains = ["weibo.com"]
	start_urls = [
		# "http://192.168.1.108:8080/json/index.json"
		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
  		# "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        # "https://api.weibo.com/2/statuses/user_timeline.json?screen_name=-Luxe&access_token=2.00XIqViCoblvpD87e9d1d4850Dtyjx"
        "http://scrapy.org"
	]

	def __init__(self, category=None, *args, **kwargs):
		super(WbSpider, self).__init__(*args, **kwargs)
		# print args
		# print kwargs

	

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
		item = CrawlerItem()
		item['titile'] = 'crawl titile'
		item['link'] = 'crawl link'
		item['desc'] = 'crawl desc'
		return item

		# test proxy
		print response.body










