# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.utils.project import get_project_settings

from porn.items import PornItem


class PornMongodbPipeline(object):

    def __init__(self):
        settings = get_project_settings()
        client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        db = client[settings['MONGO_DB']]
        # client[settings['MONGO_DB']].authenticate(name=settings['MONGO_USER'], password=settings['MONGO_PWD'],
        #                                           mechanism="SCRAM-SHA-1")
        self.coll = db[settings['MONGO_COLL']]

    def process_item(self, item, spider):
        try:
            if isinstance(item, PornItem):
                self.coll.save(dict(item))
        except Exception:
            pass
        return item
