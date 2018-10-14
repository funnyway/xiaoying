# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class XiaoyingItem(scrapy.Item):
    # define the fields for your item here like:
    # 
	project_name = scrapy.Field()
	project_id = scrapy.Field()
	year_rate = scrapy.Field()
	total_amount = scrapy.Field()
	year_rate = scrapy.Field()
	time_limit = scrapy.Field()
	ctime = scrapy.Field()
	ctime_timestamp = scrapy.Field()


