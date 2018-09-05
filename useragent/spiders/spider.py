# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/3 17:13
@Author  : ZZINDS
@Site    :
@File    : spider.py
@Software: PyCharm
"""
import scrapy

from useragent.items import UseragentItem




class UaSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["developers.whatismybrowser.com"]
    url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/firefox/'
    offset = 0
    # 起始url
    start_urls = [url + str(offset)]
#    start_urls = (
#        'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/',
#    )

    # 在所有的请求发生之前执行
    def start_requests(self):
        for url in self.start_urls:
            headers = {
                "User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"}
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse(self, response):
        #ua_name = response.url.split('=')[-1]
#        for version in response.xpath('//tbody//tr//td[2]/text()').extract():
#            item = UseragentItem()
#            version = version.strip()
#
#        for hardware in response.xpath('//tbody//tr//td[4]/text()').extract():
#            hardware = hardware.strip()
#
        for ua in response.xpath('//td/a/text()').extract():
            item = UseragentItem()
            #item['ua_name'] = ua_name
            #version = response.xpath('//tbody//tr//td[2]/text()')
            #hardware = response.xpath('//tbody//tr//td[4]/text()')
            item['ua'] = ua.strip()
            yield item

        if self.offset < 8:
            self.offset += 1
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)