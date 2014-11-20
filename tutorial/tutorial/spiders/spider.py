# -*- coding: utf-8 -*-
import chardet
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.utils.url import urljoin_rfc
from scrapy.http import Request
from tutorial.items import bbsItem

class bbsSpider(BaseSpider):
    name = "boat"
    allowed_domains = ["bbs.nju.edu.cn"]
    start_urls = ["http://bbs.nju.edu.cn/bbstop10"]
    def parseContent(self,content):
        content = content[0].encode('utf-8')
        #print chardet.detect(content)
        #print content
        authorIndex =content.index('信区')
        author = content[11:authorIndex-2]
        boardIndex = content.index('标 题')
        board = content[authorIndex+8:boardIndex-2]
        timeIndex = content.index('南京大学小百合站 (')
        time = content[timeIndex+26:timeIndex+50]
        return (author,board,time)
    #content = content[timeIndex+58:]
    #return (author,board,time,content)
    def parse2(self,response):
        hxs =HtmlXPathSelector(response)
        item = response.meta['item']
        items = []
        content = hxs.select('/html/body/center/table[1]/tr[2]/td/textarea/text()').extract()
        parseTuple = self.parseContent(content)
        item['author'] = parseTuple[0].decode('utf-8')
        item['board'] =parseTuple[1].decode('utf-8')
        item['time'] = parseTuple[2]
        #item['content'] = parseTuple[3]
        items.append(item)
        return items
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        title= hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/text()').extract()
        url= hxs.select('/html/body/center/table/tr[position()>1]/td[3]/a/@href').extract()
        for i in range(0, 10):
            item = bbsItem()
            item['link'] = urljoin_rfc('http://bbs.nju.edu.cn/', url[i])
            item['title'] = title[i][:]
            items.append(item)
        for item in items:
            yield Request(item['link'],meta={'item':item},callback=self.parse2)

