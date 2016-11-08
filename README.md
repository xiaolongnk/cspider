#cspider

爬虫项目，基于scrappy实现。


## 配置

1. setting.py  配置文件，里面可以设置 USER_AGENT ,伪装成browser，防止被拒。
    如果没有这个配置的话，stackoverflow的那个spider会被403拒绝。



### spiders

1. blognofile 

        根据sitemap.xml 抓取网站，抓取了我的博客的[sitemap](https://blog.nofile.cc/sitemap.xml)。
        重要灵感来自这里[官方docs](http://scrapy-chs.readthedocs.io/zh_CN/latest/topics/spiders.html#id2)
        采用xpath模式。

2. stackoverflow
        
        这也是一个比较经典的例子,抓取了stackoverflow上的问题。采用了css模式。


### 数据存储

抓取的数据以json形式存放在data目录下，json文件名和spider的名字保持一致。


### 参考资料

1. https://doc.scrapy.org/en/latest/topics/selectors.html
2. http://chenqx.github.io/2014/12/23/Spider-Advanced-for-Dynamic-Website-Crawling/
3. http://snowdream1314.github.io/2016/02/19/scrapy-1/
