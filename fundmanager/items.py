# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Manager(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    appointment_date = scrapy.Field()
    introduction = scrapy.Field()
    company = scrapy.Field()
    fund_asset_size = scrapy.Field()
    sex = scrapy.Field()
    picture = scrapy.Field()
    funds = scrapy.Field()


class Fund(scrapy.Item):
    code = scrapy.Field()
    name = scrapy.Field()
    type = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    duty_days = scrapy.Field()
    duty_return = scrapy.Field()
    average = scrapy.Field()
    rank = scrapy.Field()
    manager = scrapy.Field()

class FundmanagerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass