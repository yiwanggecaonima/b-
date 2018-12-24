# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import pymysql


from bili.items import BiliItem,douga,anime,guochang,music,dance,game,technology,life,kichiku,fashion,ent,cinephile


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db


    @classmethod
    def from_crawler(cls, crawler):
        return cls(mongo_uri=crawler.settings.get('MONGO_URI'), mongo_db=crawler.settings.get('MONGO_DB'))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self,item,spider):
        if isinstance(item,BiliItem):
            collection = 'BiliItem'
            if self.db[collection].insert(item):
                print('ojbk ...... ')
        if isinstance(item,douga):
            collection = 'douga'
            if self.db[collection].update({'aid':item['aid']},dict(item),True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,anime):
            collection = 'anime'
            if self.db[collection].update({'aid':item['aid']},dict(item),True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,guochang):
            collection = 'guochang'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,dance):
            collection = 'dance'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,game):
            collection = 'game'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,music):
            collection = 'music'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,technology):
            collection = 'technology'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,life):
            collection = 'life'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,kichiku):
            collection = 'kichiku'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,fashion):
            collection = 'fashion'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,ent):
            collection = 'ent'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')
        elif isinstance(item,cinephile):
            collection = 'cinephile'
            if self.db[collection].update({'aid': item['aid']}, dict(item), True):
                print('Sueecss saved to Mongo ......')

        return item

    def close_spider(self, spider):
        self.client.close()


class MysqlPipeline(object):
    def __init__(self, mysql_uri, mysql_db,mysql_port,mysql_user,mysql_pass,mysql_charset):
        self.mysql_uri = mysql_uri
        self.mysql_db = mysql_db
        self.mysql_port = mysql_port
        self.mysql_user=mysql_user
        self.mysql_pass = mysql_pass
        self.mysql_charset = mysql_charset

    @classmethod
    def from_crawler(cls, crawler):
        return cls(mysql_uri=crawler.settings.get('MYSQL_URI'), mysql_db=crawler.settings.get('MYSQL_DB'),
                   mysql_port=crawler.settings.get('MYSQL_PORT'),mysql_pass=crawler.settings.get('MYSQL_PASS'),
                   mysql_user=crawler.settings.get('MYSQL_USER'),mysql_charset=crawler.settings.get('MYSQL_CHARSET'))


    def open_spider(self, spider):
        self.conn = pymysql.connect(host=self.mysql_uri,port=self.mysql_port,user=self.mysql_user,passwd=self.mysql_pass,db=self.mysql_db,charset=self.mysql_charset)
        self.cur = self.conn.cursor()

    def process_item(self,item,spider):

        if isinstance(item,BiliItem):
            sql = 'replace into BiliItem values(%s,%s,%s,%s);'
            values = (item['b_cate_name'],item['b_cate_link'],item['m_cate_name'],item['m_cate_link'])
            self.cur.execute(sql,values)

        elif isinstance(item,douga):
            sql = 'replace into douga values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
            item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
            item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
            item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item,anime):
            sql = 'replace into anime values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (item['aid'],item['tid'],item['tname'],item['pic'],item['title'],item['descs'],item['pubdate'],
                      item['view'],item['danmaku'],item['name'],item['favorite'],item['face'],item['likes'],
                      item['attribute'],item['duration'],item['dynamic'])
            self.cur.execute(sql,values)

        elif isinstance(item, guochang):
            sql = 'replace into guochang values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, music):
            sql = 'replace into music values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, dance):
            sql = 'replace into dance values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, game):
            sql = 'replace into game values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'],item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, technology):
            sql = 'replace intotechnology values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, life):
            sql = 'replace into life values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, kichiku):
            sql = 'replace into kichiku values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, fashion):
            sql = 'replace into fashion values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, ent):
            sql = 'replace into ent values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'],item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        elif isinstance(item, cinephile):
            sql = 'replace into cinephile values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            values = (
                item['aid'], item['tid'], item['tname'], item['pic'], item['title'], item['descs'], item['pubdate'],
                item['view'], item['danmaku'], item['name'], item['favorite'], item['face'], item['likes'],
                item['attribute'], item['duration'], item['dynamic'])
            self.cur.execute(sql, values)

        try:
            self.conn.commit()
        except Exception:
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()




class BiliPipeline(object):
    def process_item(self, item, spider):
        return item
