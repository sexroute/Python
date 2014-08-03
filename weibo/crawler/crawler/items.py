# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    id = scrapy.Field()
    tweet = scrapy.Field()
    retweet = scrapy.Field()
    pic = scrapy.Field()
    # created_date = scrapy.Field

class CommentItem(scrapy.Item):
	id = scrapy.Field()
	comment = scrapy.Field()
	# created_date = scrapy.Field

