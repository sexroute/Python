Scrapy:
	# scrapy startproject crawler
	scrapy crawl -h
	scrapy crawl Weibo --nolog -a weibo_name=AlloVince -a depth=10 -a thread=1 -a delay=5
	scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"
	scrapy crawl Weibo --nolog -a name=-Luxe -a delay=5

Source:
	cat /usr/local/lib/python2.7/dist-packages/scrapy/spider.py
	

curl http://192.168.1.108:8080/json/index.json


workon weibo

scrapy crawl Weibo -a name=-Luxe --nolog

seq 10 | xargs -i clear







command:
scrapy crawl Weibo --nolog -a name=-Luxe -a delay=1 -s CONCURRENT_REQUESTS=1 -s DEPTH_LIMIT=3


