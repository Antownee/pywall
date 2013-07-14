#Project name = VSWallpapers
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from vswallpapers.items import VswallpapersItem

class MySpider(BaseSpider):
	name = 'vsimages'
	allowed_domains = ["www.visualstudiowallpapers.com"]
	start_urls = ["http://visualstudiowallpapers.com/"]

	def parse(self,response):
		hxs = HtmlXPathSelector(response)
		titles = hxs.select("//a[@class = 'zoomlink']")
		image_stuff = []
	
		for i in titles:
			item = VswallpapersItem()
			item['image_urls'] = i.select("@href").extract()
			image_stuff.append(item)

		return image_stuff

		print 'CRAWLING COMPLETED', image_stuff.len," wallpapers downloaded" 