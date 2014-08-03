# -*- coding: utf-8 -*-

# Scrapy settings for crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

ITEM_PIPELINES = {
	'crawler.pipelines.mysql.CrawlerPipeline':1
}

# DOWNLOADER_MIDDLEWARES = {
# 	'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 2,
# 	'crawler.middleware.proxymiddlewares.ProxyMiddleware': 3
# }


MYSQL_DB = 'test'
MYQSL_DB_USER = 'root'
MYQSL_DB_PASSWORD = 'root'

DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS = 16
DEPTH_LIMIT = 0


TEST_STR = 'ABC'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawler (+http://www.yourdomain.com)'
