#coding:utf8
from scrapy.contrib.spiders import SitemapSpider
from dirbot.items import NofileItem

'''
@author : xiaolongnk
@date   : 2016-11-02 17:08
@desc   : 根据 https://blog.nofile.cc/sitemap.xml 来抓取 blog.nofile.cc 上的所有页面。
'''
class NofileSpider(SitemapSpider):
    name = 'blognofile'
    sitemap_urls = ['https://blog.nofile.cc/sitemap.xml']

    def parse(self, response):
        item = NofileItem()
        keywords = response.selector\
                .xpath("//meta[@name='keywords']/attribute::content").extract()[0]
        description = response.selector\
                .xpath("//meta[@name='description']/attribute::content").extract()[0]
        title = response.selector\
                .xpath("//title/text()").extract()[0]
        item['url']  = response.url
        item['title'] = title
        item['keywords'] = keywords
        item['description'] = description
        self.logger.info(item)
        return item
