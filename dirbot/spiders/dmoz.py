#coding:utf8
from scrapy.spiders import Spider
from scrapy.selector import Selector
from dirbot.items import DmozItem 

'''
default scrapy spider 
'''
class DmozSpider(Spider):
    name = "dmoz"
    start_urls = [
            "http://www.mtedu.com/quanbukecheng"
    ]
    def parse(self , response):
        allitems = response.selector.xpath("//div[@class='excitem clitem']").extract()
        cnt = 0
        items = []
        for i in allitems:
            subs          = Selector(text=i)
            title         = subs.xpath("//div[@class='coursecover']/attribute::title").extract()[0]
            description     = subs.xpath("//p[@class='description']/attribute::tiel").extract()[0]
            teacher_title = subs.xpath("//span[@class='teacher']/a/attribute::title").extract()[0].strip()
            teacher_name  = subs.xpath("//span[@class='teacher']/a/text()").extract()
            if teacher_name:
                teacher_name = teacher_name[0]
            else:
                teacher_name = ""
            played        = subs.xpath("//span[@class='played']/text()").extract()[0]
            teacher_info = teacher_title+"-"+teacher_name
            cnt+=1
            print "%s==%s==%s"%(title.strip(),teacher_info.strip(),played.strip())
            item = DmozItem()
            item['title'] = title
            item['description'] = description
            item['teacher'] = teacher_info
            item['playednum'] =  played
            items.append(item)
        return items
