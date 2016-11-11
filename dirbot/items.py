from scrapy.item import Item, Field


class DmozItem(Item):

    title = Field()
    teacher= Field()
    description = Field()
    playednum = Field()


class NofileItem(Item):
    url         = Field()
    title       = Field()
    keywords    = Field()
    description = Field()


class StackOverFlowItem(Item):
    title       = Field()
    url         = Field()
    body        = Field()
    votes       = Field()
    tags        = Field()
    description = Field()
