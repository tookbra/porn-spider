# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import json
import random

from scrapy import signals
from porn.user_agents import agents


class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent


class CookiesMiddleware(object):
    """ 换cookie """
    cookie = {
        'PHPSESSID': 'pesr6vi07mq1uvf6cr7ast4vf6',
        'RNLBSERVERID': 'ded6289'
    }

    def process_request(self, request, spider):
        _cookie = json.dumps(self.cookie)
        request.cookies = json.loads(_cookie)