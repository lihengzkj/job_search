# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobgetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #公司
    company_name = scrapy.Field()

    #公司规模
    company_size = scrapy.Field()

    #地区
    company_location = scrapy.Field()

    #职位名称
    job_title = scrapy.Field()

    #任职要求
    job_requirement = scrapy.Field()

    #工资范围
    job_salary = scrapy.Field()

    #工作经验时间要求
    work_year_require = scrapy.Field()

    #经度
    company_location_lng = scrapy.Field()

    #纬度
    company_location_lat = scrapy.Field()

    #职位诱惑
    job_advantage = scrapy.Field()

    # 任职要求包含若干关键字（暂时只是6个关键字查询）
    a_key_existing = scrapy.Field()
    b_key_existing = scrapy.Field()
    c_key_existing = scrapy.Field()
    d_key_existing = scrapy.Field()
    e_key_existing = scrapy.Field()
    f_key_existing = scrapy.Field()