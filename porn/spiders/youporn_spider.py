from scrapy import Selector, Request
from scrapy.spiders import CrawlSpider

from porn.items import PornItem


class YouPornSpider(CrawlSpider):
	name = "YouPornSpider"
	start_urls = ('https://www.youporn.com/browse/time/',)
	host = 'https://www.youporn.com'


	def parse(self, response):
		selector = Selector(response)
		# xpath //子节点
		video_hrefs = selector.xpath(
			'//a[@class="video-box-image"]//@href').extract()
		print(video_hrefs)
		for href in video_hrefs:
			yield Request(url=self.host + href, callback=self.parse_porn_info)

		next_page = selector.xpath('//div[@id="next"]//div[@class="prev-next"]/a/@href').extract()
		if next_page:
			print('next page ' + self.host + next_page[0])
			yield Request(url=self.host + next_page[0], callback=self.parse)


	def parse_porn_info(self, response):
		pornItem = PornItem()
		selector = Selector(response)
		pornItem['url'] = response.url
		image_url = selector.xpath('//meta[@property="og:image"]//@content').extract()
		if image_url:
			pornItem['image_url'] = image_url[0]

		title = selector.xpath('//h1[@class="heading2"]/text()').extract()
		if title:
			pornItem['title'] = title[0]

		video_url = selector.xpath('//div[@class="mhp1138_videoWrapper"]//video/@src').extract()
		if video_url:
			pornItem['video_url'] = video_url[0]

		selector.xpath('//div[@class="video-details-inside"]//table')
		yield pornItem