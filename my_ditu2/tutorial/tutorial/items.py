# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.item import Item, Field

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#class bbsItem(Item):
#	author = Field()
#	boardIndex = Field()
#	timeIndex = Field()
#	link = Field()
#	title = Field()
#	pass


class tongjiproItem(Item):
    index = Field()
    headTitle = Field()
    description = Field()
    url = Field()

    id = Field()
    title = Field()
    link = Field()
    addtime = Field()

