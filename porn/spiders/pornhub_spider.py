import json
import re

from scrapy import Selector, Request
from scrapy.spiders import CrawlSpider
from porn.items import PornItem


class PornHubSpider(CrawlSpider):
	name = "PornHubSpider"
	start_urls = ('https://www.pornhub.com/video?o=cm',)
	host = 'https://www.pornhub.com'

	def parse(self, response):
		selector = Selector(response)
		divs = selector.xpath('//div[@class="phimage"]')
		for div in divs:
			viewkey = re.findall('viewkey=(.*?)"', div.extract())
			yield Request(url='https://www.pornhub.com/embed/%s' % viewkey[0],
			              callback=self.parse_porn_info)

		url_next = selector.xpath('//a[@class="orangeButton" and text()="Next "]/@href').extract()
		if url_next:
			yield Request(url=self.host + url_next[0],callback=self.parse)

	def parse_porn_info(self, response):
		pornItem = PornItem()
		selector = Selector(response)
		_ph_info = re.findall('flashvars_.*?=(.*?);\n', selector.extract())
		_ph_info_json = json.loads(_ph_info[0])
		duration = _ph_info_json.get('video_duration')
		pornItem['video_duration'] = duration
		title = _ph_info_json.get('video_title')
		pornItem['title'] = title
		image_url = _ph_info_json.get('image_url')
		pornItem['image_url'] = image_url
		url = _ph_info_json.get('link_url')
		pornItem['url'] = url
		video_url = _ph_info_json.get('quality_480p')
		pornItem['video_url'] = video_url
		yield pornItem