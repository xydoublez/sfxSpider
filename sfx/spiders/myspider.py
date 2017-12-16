# -*- coding: utf-8 -*-
import scrapy

from sfx.items import SfxItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['lizhiqiang.name']
    start_urls = ['http://lizhiqiang.name/']
    close_down = False

    def parse(self, response):
        request = scrapy.Request(response.url, callback=self.parsePageContent)
        yield request

    # 解析每一页的列表
    def parsePageContent(self, response):
        for sel in response.xpath('//h2[@class="entry-title"]'):
            item = SfxItem()
            item['href'] = sel.css('a::attr("href")')
            print(item['href'])
            item['text'] = sel.xpath('.//a[1]/text()').extract()[0]
            print(item['text'])
