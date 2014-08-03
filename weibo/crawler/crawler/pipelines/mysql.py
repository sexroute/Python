# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors


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
		print '--------------------process_item-----------------------'
		print item
		query = self.dbpool.runInteraction(
			self._conditional_insert,
			item)
		query.addErrback(self.handle_error)
		return item


	def _conditional_insert(self,tx,item):
		tx.execute("select * from dmoz where link = %s",(item['link'],))
		result = tx.fetchone()
		if result:
			log.msg("Item already stored in db: '%s'" % item, level=log.DEBUG)
		else:
			tx.execute("insert into dmoz (titile,link,description,created) values (%s,%s,%s,%s)",(item['titile'],item['link'],item['desc'],datetime.datetime.now()))
			log.msg("Item stored in db: %s " % item, level=log.DEBUG)

	def handle_error(self,e):
		log.err(e)

