# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import re
import urllib
import json
import codecs
import urllib.request
import requests
from scrapy.pipelines.images import ImagesPipeline
from scrapy.spiders import Request


class KzPipeline(object):

    # def __init__(self):
    #     self.file = codecs.open('../kzrush.json','a+',encoding='utf-8')

    def process_item(self, item, spider):
        f1 = open('../screenshors.txt', 'a+')
        f1.write(item['map_title'] + ' ' + item['ss_num'] + '\n')
        f2 = open('../shortcuts.txt', 'a+')
        f2.write(item['map_title'] + ' ' + item['sc_num'] + '\n')
        f1.close()
        f2.close()
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(line)
        return item

    # def spider_closed(self, spider):
    #     self.file.close()
    def close_spider(self, spider):
        print("|", "下载完毕！".center(30, "*"), "|")

class ImgPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        '''获取图片的url,通过Request方法，保存图片'''

        # 这里meta={'item': item},目的事件item传递到file_path中
        for i in item['screenshots']:
            #print('正在下载++++++++')
            yield Request(i, meta={'item':item,'url':i})
            #print("下载成功！")
        for j in item['shortcuts']:
            yield Request(j, meta={'item':item,'url':j})
    def file_path(self, request, response=None, info=None):
        '''图片保存的路径'''
        item = request.meta['item']
        imgurl = request.meta['url']
        apath = "./" + item["map_title"]
        #img_name = imgurl
        img_name = re.findall('(screenshots|shortcuts)+(\S+)+.jpg',imgurl)[0]
        path = apath + '/' + img_name[0] + img_name[1] +  '.jpg'
        #print("图片路径+++++++++++++", path)
        return path

