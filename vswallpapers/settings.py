# Scrapy settings for vswallpapers project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'vswallpapers'

SPIDER_MODULES = ['vswallpapers.spiders']
NEWSPIDER_MODULE = 'vswallpapers.spiders'
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline']
IMAGES_STORE = 'C:\Users\Anthony\Desktop\DreamBox\Nerdery\Code\Python\VSWallpapers\images'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'vswallpapers (+http://www.yourdomain.com)'
