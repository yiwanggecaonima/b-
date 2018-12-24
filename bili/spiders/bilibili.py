# -*- coding: utf-8 -*-
from scrapy import Spider,Request
from scrapy_redis.spiders import RedisCrawlSpider

from bili.items import BiliItem,douga,anime,guochang,music,dance,game,technology,life,kichiku,fashion,ent,cinephile
import requests
import json
import re

class BilibiliSpider(RedisCrawlSpider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']  # 此处可以来个动态域
    redis_key = 'crawl_bili'
    # start_urls = ['https://www.bilibili.com/']
    # def start_requests(self):
    #     for base_url in self.start_urls:
    #         yield Request(base_url,callback=self.parse)


    def parse(self, response):
        # print(response.xpath("//ul[@class='nav-menu']/li/a/div[@class='nav-name']/text()").extract())

        for b_list in response.xpath("//ul[@class='nav-menu']/li[position()<16 and position()>1]"):
            item = BiliItem()
            b_cate_name = b_list.xpath(".//div[@class='nav-name']/text()").extract_first()
            b_cate_link = b_list.xpath("./a/@href").extract_first().lstrip('//')
            item['b_cate_name'] = b_cate_name
            item['b_cate_link'] = b_cate_link
            m_cate_name = ''
            item['m_cate_name'] = m_cate_name
            m_cate_link = b_list.xpath("./ul/li/a/@href").extract() if b_list.xpath("./ul/li/a/@href") else None
            item['m_cate_link'] = m_cate_link
            if item['m_cate_link']:
                for link in item['m_cate_link']:
                    link = 'http:' + link
                    yield Request(link,callback=self.parse_item)

    def parse_item(self,response):
        if 'douga' in response.url:
            self.item = douga()
        elif 'anime' in response.url:
            self.item = anime()
        elif 'guochang' in response.url:
            self.item = guochang()
        elif 'music' in response.url:
            self.item = music()
        elif 'dance' in response.url:
            self.item = dance()
        elif 'game' in response.url:
            self.item = game()
        elif 'technology' in response.url:
            self.item = technology()
        elif 'life' in response.url:
            self.item = life()
        elif 'kichiku' in response.url:
            self.item = kichiku()
        elif 'fashion' in response.url:
            self.item = fashion()
        elif 'ent' in response.url:
            self.item = ent()
        elif 'cinephile' in response.url:
            self.item = cinephile()
        print('当前获取url.........',response.url.split('/')[-3],'......',)
        print('\n' * 3)
        li_list = response.xpath("//div[@class='tag-list-cnt']/ul/li")[1:]
        if li_list:
            p = re.compile(r'"tid":(\d+)')
            tids = re.findall(p,response.text)[1:]
            d = re.compile(r'"tag_id":(\d+)')
            tag_ids = re.findall(d,response.text)
            for tid in tids:

                for tag_id in tag_ids:
                    get_page = 'https://api.bilibili.com/x/tag/ranking/archives?tag_id={}&rid={}&type=0&ps=20'.format(tag_id,tid)

                    res = requests.get(get_page)
                    print('...........正在获取页数.................')
                    print('\n' * 3)
                    page_num = int(int(json.loads(res.text)['data']['page']['count']) / 20) + 1
                    for page in range(1, page_num):
                        next_page = 'https://api.bilibili.com/x/tag/ranking/archives?tag_id={}&rid={}&type=0&pn={}&ps=20'.format(tag_id, tid, page)
                        yield Request(next_page,callback=self.parse_content,meta={'item':self.item})



                        # li_list = response.xpath("//div[@class='tag-list-cnt']/ul/li")[1:]
        # if li_list:
        #     for li in li_list:
        #         li_link = li.xpath("./a/@href").extract_first()
        #         link = response.url + li_link
        #         yield Request(link,callback=self.parse_detail)

        # else:
        #     li_list = response.xpath("//ul[@class='clearfix']/li").extract()[1:]
        #     for li in li_list:
        #         li_link = 'http:' + li.xpath("./a/@href").extract_first()
                # yield Request(li_link,callback=self.parse_all

    def parse_content(self,response):
        print(response.url)
        item = response.meta['item']
        datas = json.loads(response.text)["data"]["archives"]
        for data in datas:
            item['aid'] = data['aid']
            item['tid'] = data['tid']
            item['tname'] = data['tname']
            item['pic'] = data['pic']
            item['title'] = data['title']
            item['descs'] = data['desc']
            item['pubdate'] = data['pubdate']
            item['view'] = data['stat']['view']
            item['danmaku'] = data['stat']['danmaku']
            item['name'] = data['owner']['name']
            item['favorite'] = data['stat']['favorite']
            item['face'] = data['owner']['face']
            item['likes'] = data['stat']['like']
            item['attribute'] = data['attribute']
            item['duration'] = data['duration']
            item['dynamic'] = data['dynamic']
        yield item

    # def parse_detail(self,response):
    #     print(response.url)












