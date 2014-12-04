# -*- coding: utf-8 -*-
from scrapy.contrib.spiders             import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from scrapy.spider    import BaseSpider
from scrapy.selector  import Selector
from scrapy.utils.url import urljoin_rfc
from scrapy.http      import Request
from tutorial.items   import tongjiproItem
from scrapy.selector import HtmlXPathSelector

import chardet
import sys
add = 0
sys.stdout = open('resulte.txt','w')

class tongjiSpider(BaseSpider):
    name = "tongji"
    allowed_domains = ['www.stats.gov.cn']
    #start_urls = ["http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013"]
    start_urls = [
        #"http://www.stats.gov.cn/tjsj",
        "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html"
    ]

    def parse(self,response):
        items = []
        #item = Website()
        #item['index'] = sel.xpath('//tr[@class=\'provincetr\']/td/a[@href]/text()').extract()
        hxs=HtmlXPathSelector(response)
        sites=hxs.select('//tr[@class=\'provincetr\']/td')
    #    item['url'] = response

        global add
        for site in sites:
            add+=1
            item=tongjiproItem()
            item['id']=add
            item['title']=site.select('a/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['addtime']=site.select('span/text()').extract()
            items.append(item)

        return items


    rules = (
        Rule(SgmlLinkExtractor(allow=('/tr[@class=\'provincetr\']/td/a[@href]/text()',),)),
#        Rule(SgmlLinkExtractor(allow=('tjsj/tjbz/tjyqhdmhcxhfdm/2013/\?page\=([\w+])', ),)),
#        Rule(SgmlLinkExtractor(allow=('huhuuu/default.html\?page\=([\w]+)', ),)),
#        Rule(SgmlLinkExtractor(allow=('huhuuu/p/', )), callback='parse_item'),
#        Rule(SgmlLinkExtractor(allow=('huhuuu/archive/', )), callback='parse_item'), #以前的一些博客是archive形式的所以
        )

    def parse_province(self,response):

        return item
