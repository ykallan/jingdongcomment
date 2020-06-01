# -*- coding: utf-8 -*-
import scrapy
from ..items import JdcommentItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']
    haoping = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100000177760&score=3&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1'
    # zhongping = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100000177760&score=2&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    chaping = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100000177760&score=1&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'
    # 好评中评差评 scroe决定 翻页page
    commen_url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100000177760&score={}&sortType=5&page={}&pageSize=10&isShadowSku=0&fold=1'
    '''
    commen_url = [haoping, zhongping, chaping]
    commen_type = ['好评','中评','差评']
    def start_requests(self):
        for type, url in zip(self.commen_type, self.commen_url):
            meta = {'type':type}
            yield scrapy.Request(url=url, callback=self.parse,meta=meta)
    '''
    def start_requests(self):
        for score in [1,2,3]:
            if score == 1:
                meta = {'type': '差评'}
                for page in range(1,100):
                    yield scrapy.Request(url=self.commen_url.format(score, page), callback=self.parse, meta=meta)

            if score == 2:
                meta = {'type': '中评'}
                for page in range(1,100):
                    yield scrapy.Request(url=self.commen_url.format(score, page), callback=self.parse, meta=meta)

            if score == 3:
                meta = {'type': '好评'}
                for page in range(1,100):
                    yield scrapy.Request(url=self.commen_url.format(score, page), callback=self.parse, meta=meta)

    def parse(self, response):
        item = JdcommentItem()
        null = 'null'
        true = True
        false = False
        commen_type = response.meta['type']

        resp = eval(response.text[20:-2])

        for comment in resp['comments']:
            # print(comment)
            item['commen_type'] = commen_type
            item['id'] = comment['id']
            item['guid'] = comment['guid']
            item['content'] = comment['content']
            item['creationTime'] = comment['creationTime']
            item['isDelete'] = comment['isDelete']
            item['isTop'] = comment['isTop']
            item['userImageUrl'] = comment['userImageUrl']
            item['topped'] = comment['topped']
            yield item

