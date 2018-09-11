# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


#class UseragentPipeline(object):
#    def process_item(self, item, spider):
#        return item
import json


class UseragentPipeline(object):

#    def __init__(self):
#        self.wb = Workbook
#        self.ws = self.wb.active
#
#
#
#    def process_item(self, item, spider):  # 工序具体内容
#        line = [item['ua'], item['version'], item['hardware']]  # 把数据中每一项整理出来
#        self.ws.append(line)  # 将数据以行的形式添加到xlsx中
#        self.wb.save('nmsl.xlsx')  # 保存xlsx文件
#        return item
#
#    def spider_close(self,spider):
#
#        self.con.close()
    def __init__(self):
        self.file = open('items.csv', 'wb')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()