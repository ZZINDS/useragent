# -*- coding: utf-8 -*-
"""
@Time    : 2018/9/3 17:13
@Author  : ZZINDS
@Site    :
@File    : spider.py
@Software: PyCharm
"""
import scrapy
import random
from useragent.items import UseragentItem




class UaSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["developers.whatismybrowser.com"]
    url = 'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/'
    offset = 1850
    # 起始url
    start_urls = [url + str(offset)]
#    start_urls = (
#        'https://developers.whatismybrowser.com/useragents/explore/software_name/chrome/',
#    )

    # 在所有的请求发生之前执行
    def start_requests(self):
        user_agent_lint =  [ "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/60.0.3112.113 Safari/537.36",
                   "Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4)\AppleWebKit/537.36(KHTML, like Gecko) Chrome/52 .0.2743. 116 Safari/537.36",
                   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/60.0.3112.90 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)"]
        user_agent = random.choice(user_agent_lint)  # 随机ua
        for url in self.start_urls:
            headers = {"User-Agent": user_agent}
            print user_agent
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def parse(self, response):
        #ua_name = response.url.split('=')[-1]
#        for version in response.xpath('//tbody//tr//td[2]/text()').extract():
#            item = UseragentItem()
#            version = version.strip()
#
#        for hardware in response.xpath('//tbody//tr//td[4]/text()').extract():
#            hardware = hardware.strip()
        for hardware in response.xpath('//tbody//tr//td[4]/text()').extract():
            item = UseragentItem()
            item['hardware'] = hardware.strip()
            yield item
            #item = UseragentItem()
            #item['ua_name'] = ua_name
            #version = response.xpath('//tbody//tr//td[2]/text()')
            #hardware = response.xpath('//tbody//tr//td[4]/text()')
            #item['ua'] = ua.strip()
            #yield item

        if self.offset < 2:
            self.offset += 1
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)