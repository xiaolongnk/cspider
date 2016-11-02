from scrapy.item import Item, Field


class DmozItem(Item):

    url         = Field()
    name        = Field()
    keywords    = Field()
    description = Field()


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
