# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import  Item, Field


class PornItem(Item):
    image_url = Field()
    url = Field()
    video_url = Field()
    title = Field()
    upload_time = Field()
    visit_count = Field()
    video_duration = Field()