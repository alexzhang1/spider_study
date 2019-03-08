# -*- coding: utf-8 -*-
import sys
import io
from scrapy import Spider,Request
import requests
import re
from lxml import etree
import json
from urllib import quote
from lianjia.items import LianjiaItem




# # Request中meta参数的作用是传递信息给下一个函数
# response = Request(url=url, meta={'region': region1})  # 用来获取页码
# print response.method
# region = response.meta['region']
# selector = etree.HTML(response.text)
# sel = selector.xpath("//div[@class='page-box house-lst-page-box']/@page-data")[0]  # 返回的是字符串字典
# sel = json.loads(sel)  # 转化为字典
# total_pages = sel.get("totalPage")
def start_requests(url):
    #url = "https://nj.lianjia.com/xiaoqu/" + region + "/"
    region = "gulou"
    # Request中meta参数的作用是传递信息给下一个函数
    response = Request(url=url, meta={'region': region})  # 用来获取页码
    #response = requests.get(url)
    return response


def parse(response):
    #region = response.meta['region']
    selector = etree.HTML(response.text)
    sel = selector.xpath("//div[@class='page-box house-lst-page-box']/@page-data")[0]  # 返回的是字符串字典
    sel = json.loads(sel)  # 转化为字典
    print "sel"
    total_pages = sel.get("totalPage")
    return total_pages

def parse_xiaoqu(response):
    selector = etree.HTML(response.text)
    xiaoqu_list = selector.xpath('//ul[@class="listContent"]//li//div[@class="title"]/a/text()')
    housecode_list = selector.xpath('//ul[@class="listContent"]//li/@data-housecode')
    return housecode_list

reload(sys)
sys.setdefaultencoding('utf-8')
region1 ="gulou"
housecode = '5011102208360'
url = "https://nj.lianjia.com/xiaoqu/" + region1 + "/"
url_page = "https://nj.lianjia.com/xiaoqu/" + region1 + "/pg1/"
url_xiaoqu_cj_housecode = "https://sh.lianjia.com/chengjiao/pg1" + "c" + housecode + "/"
print "house_code_url_c:", url_xiaoqu_cj_housecode
allowed_domains = ['nj.lianjia.com']
#city = allowed_domains[0].split(".")[0]
city = url.split('//')[1].split('.')[0]
# print city
dict = {'Name': 'Zara', 'Age': 7, 'Class': '五年级'}
seq = dict.values()
# print seq
# file = open('test.txt', 'w')
# list2=[]
# for line in seq:
#     if isinstance(line,int):
#         tem = str(line)
#     else:
#         tem = line
#     #file.write(tem+',')
#     list2.append(tem)
#     #print type(list2)
# file.writelines(','.join(list2)+'\n')
# file.close()



# resp1 = start_requests(url_page)
# print resp1
# print type(resp1)
# xiaoqu_list = parse_xiaoqu(resp1)
# print len(xiaoqu_list)
# for list in xiaoqu_list:
#     print list
# total_pages = parse(resp1)
# print "toal_pages:", total_pages
xiaoqu = "浦沁苑"
print xiaoqu.encode()
tem = quote(xiaoqu)
url2 = "https://sh.lianjia.com/chengjiao/rs" + quote(xiaoqu) + "/"
print url2

# item1 = 'a'
# content = [u'\u8ddd2\u53f7\u7ebf\u5965\u4f53\u4e1c844\u7c73']
# print "content:", content
# if len(content):
#     for i in content:
#         # 找到了返回的是非-1得数，找不到的返回的是-1
#         print i
#         if i.find("房屋满") != -1:
#             item1 = i
#         elif i.find("号线") != -1:
#             item2 = i
#         elif i.find("学") != -1:
#             item3 = i
#     print "item1:", item1
#     print "item2:", item2
#     print "item3:", item3





def get_ip(order_id):
    url = "http://tvp.daxiangdaili.com/ip/?"
    try:
        response = requests.get(url+'tid='+order_id+'&num=1&delay=5')
    except:
        return None
    content = response.content
    print content
    return content

# 获取IP
order_id_num = '558408396946207'
# if len(self.ip_list) >= 5:
#     ips = random.choice(self.ip_list)
# else:
#     ips = get_ip(order_id_num)
ips = get_ip(order_id_num)
temp = "http://" + ips
print "temp:", temp

list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4 ]
for (l1,l2) in zip(list1,list2):
    print str(l1) + "join" + str(l2)