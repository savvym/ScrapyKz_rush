import scrapy
import re
from scrapy import Request
from ..items import KzItem
from scrapy.selector import Selector


class KzSpider(scrapy.Spider):
    name = 'kz'
    allowed_domains = ["kz-rush.ru"]
    file = open('./kzrush.txt')
    urllist = file.readlines()
    start_urls = []
    #start_urls = ['https://kz-rush.ru/en/maps/cs16/8b1_brickngrass']
    for u in urllist:
        u = re.sub(r'\n','',u)
        start_urls.append(u)

    def parse(self, response):
        url = "https://kz-rush.ru"
        sel = Selector(response)
        item = KzItem()
        item['map_title'] = \
            sel.xpath('/html/body/div/div[1]/div[1]/section/div[1]/strong/text()').extract()[0]
        item['map_screenshots'] = \
            sel.xpath('/html/body/div/div[1]/div[1]/section/table/tr[3]/td/div/ul/li[1]/a/text()').extract()[0]
        item['ss_num'] = re.findall('\d+', item['map_screenshots'])[0]
        item['screenshots'] = \
            sel.xpath('//*[@id="mapscreenshots"]/ul').re('/xr_public/upload/maps/screenshots/thumbnails/\S*.jpg')
        for i in range(len(item['screenshots'])):
            item['screenshots'][i] = url + item['screenshots'][i].replace('/thumbnails', '')
        item['map_shortcuts'] = \
            sel.xpath('/html/body/div/div[1]/div[1]/section/table/tr[3]/td/div/ul/li[2]/a/text()').extract()[0]
        item['sc_num'] = re.findall('\d+', item['map_shortcuts'])[0]
        item['shortcuts'] = \
            sel.xpath('//*[@id="mapshortcuts"]/ul').re('/xr_public/upload/maps/shortcuts/thumbnails/\S*.jpg')
        for i in range(len(item['shortcuts'])):
            item['shortcuts'][i] = url + item['shortcuts'][i].replace('/thumbnails','')

        yield item
