# -*- coding: utf-8 -*-

# Scrapy settings for porn project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'porn'

SPIDER_MODULES = ['porn.spiders']
NEWSPIDER_MODULE = 'porn.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1.5 # 间隔时间
CONCURRENT_REQUESTS = 16  # 默认为16

DOWNLOADER_MIDDLEWARES = {
	'porn.middlewares.UserAgentMiddleware': 400,
	'porn.middlewares.CookiesMiddleware': 401,
}

ITEM_PIPELINES = {
    'porn.pipelines.PornMongodbPipeline': 403,
}

MONGO_HOST = 'mongodb'
MONGO_PORT = 27017
MONGO_DB = 'porn'
MONGO_COLL = 'porn_info'

LOG_FILE = 'log/spider.log'
LOG_LEVEL = 'INFO'
LOG_STDOUT = True

