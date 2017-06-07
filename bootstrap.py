# from scrapy import cmdline

# cmdline.execute("scrapy crawl RedTubeSpider".split())
# cmdline.execute("scrapy crawl YouPornSpider".split())
# cmdline.execute("scrapy crawl RedTubeSpider".split())


from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from porn.spiders.pornhub_spider import PornHubSpider
from porn.spiders.redtube_spider import RedTubeSpider
from porn.spiders.youporn_spider import YouPornSpider


porcess = CrawlerProcess(get_project_settings())
porcess.crawl(PornHubSpider)
porcess.crawl(RedTubeSpider)
porcess.crawl(YouPornSpider)

porcess.start();