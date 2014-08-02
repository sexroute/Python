Scrapy:
	# scrapy startproject crawler
	scrapy crawl -h
	scrapy crawl Weibo --nolog -a weibo_name=AlloVince -a depth=10 -a thread=1 -a delay=5
	scrapy shell "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/"

Source:
	cat /usr/local/lib/python2.7/dist-packages/scrapy/spider.py
	

curl http://192.168.1.108:8080/json/index.json


workon weibo



sed -i 's/properties/property/g' text.sh
