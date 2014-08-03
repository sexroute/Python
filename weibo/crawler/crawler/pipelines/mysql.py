# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from twisted.enterprise import adbapi
from datetime import datetime
import MySQLdb.cursors
import json
from crawler.items import CrawlerItem,CommentItem
from crawler.utils import encodeconvert


class CrawlerPipeline(object):
	def __init__(self,db,dbuser,dbpassword):
		self.dbpool = adbapi.ConnectionPool(
			'MySQLdb',
			db=db,
			user=dbuser,
			passwd=dbpassword,
			cursorclass=MySQLdb.cursors.DictCursor,
			charset='utf8', 
			use_unicode=True)

	@classmethod
	def from_crawler(cls, crawler):
		db = crawler.settings.get('MYSQL_DB')
		dbuser = crawler.settings.get('MYQSL_DB_USER')
		dbpassword = crawler.settings.get('MYQSL_DB_PASSWORD')
		return cls(db,dbuser,dbpassword)


	def process_item(self, item, spider):
		# print spider.settings.get('MYSQL_DB')
		if type(item) == CrawlerItem:
			self.dbpool.runInteraction(self.tweet_inset,item).addErrback(self.handle_error)
			return item
		elif type(item) == CommentItem:
			self.dbpool.runInteraction(self.comment_inset,item).addErrback(self.handle_error)
		# return item

	def tweet_inset(self,tx,item):
		tx.execute("select 1 from tweet where id=%s",(item.get('id'),))
		result = tx.fetchone()
		if result:
			log.msg("tweet is already stored: '%s'" % item.get('tweet'),level=log.DEBUG)
		else:
			tx.execute("insert into tweet (id,tweet,created_date) values (%s,%s,%s) ",(item.get('id'),item.get('tweet'),datetime.now()))
			log.msg("tweet stored: %s" % item.get('tweet'),level=log.DEBUG)

	def comment_inset(self,tx,item):
		tx.execute("select 1 from comment where id=%s and comment=%s",(item.get('id'),item.get('comment')))
		result = tx.fetchone()
		if result:
			log.msg("comment is already stored: '%s'" % item.get('comment'),level=log.DEBUG)
		else:
			tx.execute("insert into comment (id,comment,created_date) values (%s,%s,%s) ",(item.get('id'),item.get('comment'),datetime.now()))
			log.msg("comment stored: %s" % item.get('comment'),level=log.DEBUG)

	def handle_error(self,e):
		log.err(e)

