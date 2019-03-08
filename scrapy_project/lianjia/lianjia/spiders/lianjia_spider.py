# -*- coding: utf-8 -*-
from scrapy import Spider,Request
import re
from lxml import etree
import json
from urllib import quote
from lianjia.items import LianjiaItem
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

class Lianjia_spider(Spider):
    name = 'lianjia'
    allowed_domains = ['sh.lianjia.com']
    # regions = {'gulou':'鼓楼',
    #            'jianye':'建邺',
    #            'qinhuai':'秦淮',
    #            'xuanwu':'玄武',
    #            'yuhuatai':'雨花台',
    #            'qixia':'栖霞',
    #            'jiangning':'江宁',
    #            'liuhe':'六合',
    #            'pukou':'浦口',
    #            'lishui':'涟水',
    #            'gaochun':'高淳'
    # }
    regions = {
               'nichengzhen':'泥城镇'
    }

    def start_requests(self):
        for region in list(self.regions.keys()):
            url = "https://sh.lianjia.com/xiaoqu/" + region + "/"
            # Request中meta参数的作用是传递信息给下一个函数
            yield Request(url=url, callback=self.parse, meta={'region':region}) #用来获取页码

    def parse(self, response):
        region = response.meta['region']
        selector = etree.HTML(response.text)
        sel = selector.xpath("//div[@class='page-box house-lst-page-box']/@page-data")[0]  # 返回的是字符串字典
        sel = json.loads(sel)  # 转化为字典
        total_pages = sel.get("totalPage")

        for i in range(int(total_pages)):
            url_page = "https://sh.lianjia.com/xiaoqu/{}/pg{}/".format(region, str(i + 1))
            yield Request(url=url_page, callback=self.parse_xiaoqu, meta={'region':region})

    def parse_xiaoqu(self,response):
        selector = etree.HTML(response.text)
        #使用小区中文名字处理
        #xiaoqu_list = selector.xpath('//ul[@class="listContent"]//li//div[@class="title"]/a/text()')
        #使用小区的housecode处理
        housecode_list = selector.xpath('//ul[@class="listContent"]//li/@data-housecode')
        #for xq_name in xiaoqu_list:
        #使用house_code
        for housecode in housecode_list:
            #housecode = "5011000013050"
            #xq_name = "云帆花苑"
            # print "xq_name:", xq_name
            # print type(xq_name)
            # tem = quote(xq_name.encode('utf8'))
            # print "tem:", tem
            # 使用小区中文名字处理
            #url = "https://sh.lianjia.com/chengjiao/rs" + quote(xq_name.encode('utf8')) + "/"
            # 使用小区的housecode处理
            url = "https://sh.lianjia.com/chengjiao/" + "c" + housecode + "/"
            # print "url:", url
            #yield Request(url=url, callback=self.parse_chengjiao, meta={'xq_name':xq_name,
            yield Request(url=url, callback=self.parse_chengjiao, meta={'housecode':housecode,
                                    'region':response.meta['region']})

    def parse_chengjiao(self,response):
        #使用中文名字处理时
        #xq_name = response.meta['xq_name']
        housecode = response.meta['housecode']
        selector = etree.HTML(response.text)
        print response.text
        content = selector.xpath("//div[@class='page-box house-lst-page-box']")  #有可能为空
        #print "content:", content
        total_pages = 0
        print housecode
        if len(content):
            page_data = json.loads(content[0].xpath('./@page-data')[0])
            total_pages = page_data.get("totalPage")  # 获取总的页面数量
            # test
            # total_pages = 1
        if(housecode == "5011000013050"):
            total_pages = 2
        for i in range(int(total_pages)):
            #url_page = "https://sh.lianjia.com/chengjiao/pg{}rs{}/".format(str(i+1), quote(xq_name.encode('utf8')))
            #print housecode
            url_page = "https://sh.lianjia.com/chengjiao/pg{}c{}/".format(str(i+1), housecode)
            print "url_page:", url_page
            yield Request(url=url_page, callback=self.parse_content, meta={'region': response.meta['region']})

    def parse_content(self,response):
        #time.sleep(3)
        selector = etree.HTML(response.text)
        cj_list = selector.xpath("//ul[@class='listContent']/li")


        for cj in cj_list:
            item = LianjiaItem()
            item['city'] = self.allowed_domains[0].split(".")[0]
            item['region'] = self.regions.get(response.meta['region'])
            href = cj.xpath('./a/@href')
            if not len(href):
                continue
            item['href'] = href[0]

            content = cj.xpath('.//div[@class="title"]/a/text()')
            if len(content):
                content = content[0].split()  # 按照空格分割成一个列表
                item['name'] = content[0]
                item['style'] = content[1]
                item['area'] = content[2]

            content = cj.xpath('.//div[@class="houseInfo"]/text()')
            if len(content):
                content = content[0].split('|')
                item['orientation'] = content[0].rstrip().lstrip()
                item['decoration'] = content[1].rstrip().lstrip()
                # 有电梯
                if len(content) == 3:
                    item['elevator'] = content[2].rstrip().lstrip()
                else:
                    item['elevator'] = '无'

            content = cj.xpath('.//div[@class="positionInfo"]/text()')
            if len(content):
                content = content[0].split()
                item['floor'] = content[0]
                if len(content) == 2:
                    item['build_year'] = content[1]
                else:
                    item['build_year'] = '无'

            content = cj.xpath('.//div[@class="dealDate"]/text()')
            if len(content):
                item['sign_time'] = content[0]

            content = cj.xpath('.//div[@class="totalPrice"]/span/text()')
            if len(content):
                item['total_price'] = content[0]

            content = cj.xpath('.//div[@class="unitPrice"]/span/text()')
            if len(content):
                item['unit_price'] = content[0]
                print "unit_price:", item['unit_price']

            item['fangchan_class'] = "None"
            item['subway'] = "None"
            item['school'] = "None"
            content = cj.xpath('.//span[@class="dealHouseTxt"]/span/text()')
            print "content:", content
            if len(content):
                for i in content:
                    # 找到了返回的是非-1得数，找不到的返回的是-1
                    if i.find("房屋满") != -1:
                        item['fangchan_class'] = i
                        #print "fangchan_class", item['fangchan_class']
                    elif i.find("号线") != -1:
                        item['subway'] = i
                        #print "subway", item['subway']
                    elif i.find("学") != -1:
                        item['school'] = i
                        #print "school:", item['school']
            yield item