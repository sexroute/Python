import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	]

	def __init__(self, category=None, *args, **kwargs):
		super(DmozSpider, self).__init__(*args, **kwargs)
		self.start_urls = ['http://www.example.com/categories/%s' % category]
		print args
		print kwargs

	def parse(self, response):
		# filename = response.url.split("/")[-2]
		# with open(filename,'wb') as f:
		# 	f.write(response.body)

		# for sel in response.xpath('//ul/li'):
		# 	titile = sel.xpath('a/text()').extract()
		# 	link = sel.xpath('a/@href').extract()
		# 	desc = sel.xpath('text()').extract()
		# 	print titile,link,desc

		items = []
		for sel in response.xpath('//ul/li'):
			item = DmozItem()
			item['titile'] = sel.xpath('a/text()').extract()
			item['link'] = sel.xpath('a/@href').extract()
			item['desc'] = sel.xpath('text()').extract()
			# yield item
		# 	print '--------------------------parse-----------------------------------'
		# 	print item
		# 	items.append(item)
		# return items

# sel.xpath('//ul/li/a/text()').extract()








