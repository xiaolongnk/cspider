from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["blog.nofile.cc"]
    start_urls = [
        "https://blog.nofile.cc/",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        self.logger.info('Hi, this is an item page! %s', response.body)
        # ans = response.xpath('//script/@src').extract()
        ans = response.xpath('//body/script').extract()

        self.logger.info("Hi, all td are here %s",ans)
        # items = []
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     self.logger.info(response.body)
        #     f.write(response.body)

        # sel = Selector(response)
        # sites = sel.xpath('//title/text()')
        # items = []
        #
        #
        # for site in sites:
        #     item = Website()
        #     item['name'] = site.xpath('//a[contains(@href, "image")]').extract()
        #     item['url'] = site.xpath('a/@href').extract()
        #     item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
        #     items.append(item)
        #
        # return items
