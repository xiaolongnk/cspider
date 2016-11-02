#coding:utf8
from scrapy.spiders import Spider

from dirbot.items import DmozItem 

'''
default scrapy spider 
'''
class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["blog.nofile.cc"]
    start_urls = [
        "https://blog.nofile.cc/sitemap.xml",
    ]
    cnt = 0
    def parse_item(self , response):

        pass

    def parse(self , response):
        pass

    '''
    def parse(self, response):
        if self.cnt == 0:
            self.cnt = self.cnt + 1
            response.selector.remove_namespaces()
            response.selector.register_namespace('blog-nofile' ,response.url)
            siteurls = response.selector.xpath('//loc/text()').extract()
            items = []
            validateurls = []
            for i in siteurls:
                validateurls.append(i)
                items.extend([self.make_requests_from_url(url).replace(callback=self.parse) 
                    for url in validateurls])
            
            '''
            先抓取sitemap.xml 中的所有链接
            '''
            return items
        else:
            title = response.selector.xpath('//title/text()').extract()[0]
            description = response.selector.xpath\
                    ("//meta[@name='description']/attribute::content").extract()[0]
            keywords = response.selector.\
                    xpath("//meta[@name='keywords']/attribute::content").extract()[0]
            item = DmozItem()
            item['name'] = title
            item['description'] = description
            item['url'] = response.url
            self.logger.info(item)
            return item
        '''
