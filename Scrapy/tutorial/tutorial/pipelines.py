# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import log
from twisted.enterprise import adbapi
import datetime
import MySQLdb.cursors

class TutorialPipeline(object):
	def __init__(self):
		self.dbpool = adbapi.ConnectionPool(
			'MySQLdb',
			db='test',
			user='root',
			passwd='root',
			cursorclass=MySQLdb.cursors.DictCursor,
			charset='utf8', 
			use_unicode=True)

	def process_item(self,item,spider):
		# print "process_item: " + item['link']
		query = self.dbpool.runInteraction(
			self._conditional_insert,
			item)
		query.addErrback(self.handle_error)
		return item

	def _conditional_insert(self,tx,item):
		print '-----------------------------_conditional_insert--------------------------------'
		print item
		tx.execute("select * from dmoz where link = %s",(item['link'],))
		result = tx.fetchone()
		if result:
			log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
		else:
			tx.execute("insert into dmoz (titile,link,description,created) values (%s,%s,%s,%s)",(item['titile'],item['link'],item['desc'],datetime.datetime.now()))
			log.msg("Item stored in db: %s " % item, level=log.DEBUG)

	def handle_error(self,e):
		log.err(e)














