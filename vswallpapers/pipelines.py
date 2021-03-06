from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class CraigsPipeline(object):
    def process_item(self, item, spider):
        return item

     def get_media_requests(self,item,info):
       	for url in item['image_urls']:
       		yield(Request(url))

     def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_urls'] = image_paths
        return item