# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KzItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    map_title = scrapy.Field()
    map_screenshots = scrapy.Field()
    ss_num = scrapy.Field()
    map_shortcuts = scrapy.Field()
    sc_num = scrapy.Field()
    screenshots = scrapy.Field()
    shortcuts = scrapy.Field()
    img_path = scrapy.Field()
    pass
