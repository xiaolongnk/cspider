#coding:utf8

import scrapy
from dirbot.items import StackOverFlowItem

'''
@author: xiaolongnk
@date  : 2016-11-02 17:07
@desc  : 抓取stackoverflow上排名帮上的第一页问题
         并获取这些问题的title,votes,body,tags,url
'''
class StackOverflowSpider(scrapy.Spider):
    name = 'stackoverflow'
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        item = StackOverFlowItem()
        item['title']       = response.selector.css('h1 a::text').extract()
        item['votes']       = response.selector.css('.question .vote-count-post::text').extract()
        item['body']        = response.selector.css('.question .post-text').extract()
        item['tags']        = response.selector.css('.question .post-tag::text').extract()
        item['description'] = ''
        item['url']         = response.url
        return item
