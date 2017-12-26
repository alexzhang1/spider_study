# -*- coding: utf-8 -*-
from selenium import webdriver
import datetime  
import time

#使用方法：
#脚本采用了PhantomJS浏览器，确保安装了PhantomJS(executable_path='D:\Anaconda2\Scripts\phantomjs.exe') 
#要秒杀的东西要首先添加在购物车中，且购物车只有这一件商品！！！ 
#配置好环境后，在程序入口处login函数填上自己的京东用户名和密码，在buy_on_time函数处设置秒杀时间，然后运行程序即可。
#要注意秒杀时间格式，并确保自己电脑时钟准确。
#脚本只是到提交订单为止，付款要自己手工付款后订单才生效。
#参考来源：http://blog.csdn.net/u013042248/article/details/53966185

def login(uname, pwd):
    obj.get("http://www.jd.com")
    obj.set_page_load_timeout(5)
    obj.find_element_by_link_text("你好，请登录").click()
    time.sleep(2)
    obj.find_element_by_link_text("账户登录").click()
    obj.find_element_by_name("loginname").send_keys(uname)
    obj.find_element_by_name("nloginpwd").send_keys(pwd)
    obj.find_element_by_id("loginsubmit").click()
    time.sleep(2)
    obj.get('https://cart.jd.com/cart.action')
    time.sleep(2)
    tempob = obj.find_element_by_class_name("submit-btn")
    tempobf = tempob.find_element_by_xpath("..")
    tempobf.click()
    tempob.click()
    time.sleep(2)
    now = datetime.datetime.now()
    print now.strftime('%Y-%m-%d %H:%M:%S')
    print 'login success'


# buytime = '2016-12-27 22:31:00' 
def buy_on_time(buytime):
    loop_flag = 1
    while (loop_flag == 1):
        print u"等待抢购中"
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            obj.find_element_by_id('order-submit').click()
            time.sleep(2)
            print now.strftime('%Y-%m-%d %H:%M:%S')
            print 'purchase success'
            loop_flag = 0
        #0.5s循环1次
        time.sleep(0.5)


def logout():    
    obj.find_element_by_class_name("icon-plus-nickname").click()
    time.sleep(1)
    obj.find_element_by_class_name("link-logout").click()
    time.sleep(1)
    print 'logout success'
    now = datetime.datetime.now()
    print now.strftime('%Y-%m-%d %H:%M:%S')

# entrance
username = raw_input(u"请输入京东用户名：\n")
password = raw_input(u"请输入用户密码：\n")

obj = webdriver.PhantomJS(executable_path='D:\Anaconda2\Scripts\phantomjs.exe')

login(username, password)
time.sleep(3)
buy_on_time('2017-12-14 14:20:00')
time.sleep(1)
logout()
#加入退出语句.20171226
obj.exit()
