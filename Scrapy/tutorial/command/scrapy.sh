Scrapy:
	scrapy crawl -h
	scrapy crawl dmoz --nolog -a weibo_name=AlloVince -a depth=10 -a thread=1 -a delay=5
	scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"

Source:
	cat /usr/local/lib/python2.7/dist-packages/scrapy/spider.py