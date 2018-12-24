# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class BiliItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    b_cate_name = Field()
    b_cate_link = Field()
    m_cate_name = Field()
    m_cate_link = Field()


class douga(Item):

    aid = Field()
    tid = Field()
    tname = Field()
    pic = Field()
    title = Field()
    descs = Field()
    pubdate = Field()
    view = Field()
    danmaku = Field()
    name = Field()
    favorite = Field()
    face = Field()
    likes = Field()
    attribute = Field()
    duration = Field()
    dynamic = Field()


class anime(douga):
    pass

class guochang(douga):
    pass

class music(douga):
    pass

class dance(douga):
    pass

class game(douga):
    pass

class technology(douga):
    pass

class life(douga):
    pass

class kichiku(douga):
    pass

class fashion(douga):
    pass

class ent(douga):
    pass

class cinephile(douga):
    pass
