# -*- coding: utf-8 -*-
#import urllib
#import urllib2
import time
import sys
import requests
import json
from tool import *
#import linecache

        
class Moper:
    
 
    #初始化，传入基地址，是否从头重新开始写入参数
    def __init__(self,Url,articleUrl,commentBaseUrl,allFlag):
        #猫扑原贴的url名称
        self.URL = Url
        #猫扑staticize的Url
        self.articleUrl = articleUrl
        #猫扑所有reply_list的commemt的url前面部分
        self.commentBaseUrl = commentBaseUrl
        #引入tool工具
        self.tool = Tool()
        #全局file变量，文件写入操作对象
        self.file = None
        #楼层标号，初始为1
        self.article_dict = {}
        #最新的楼层标号，初始为1
        self.lastfloor = 0        
        #楼层标号，初始为1
        self.floor = 0
        #从文件读取到的作者最后一次楼层
        self.fileLastfloor = 1
        #从文件读取到的上次取的总层数
        self.fileAmountfloor = 1
        #是否从头开始写入帖子所有作者的回帖内容
        self.allFlag = allFlag


    def getArticleDict(self):
        #url = 'http://staticize.mop.com/subject/getArticleById?callback=jQuery18308948445668759089_1511158138413&id=50621250&type=dzh&_=1511158138628'
        url = self.articleUrl
        headers = {
            "Host" : "staticize.mop.com",
            "Connection" : "keep-alive",
            "Accept" : "*/*",
            "X-Requested-With" : "XMLHttpRequest",
            "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Referer" : self.URL,
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            #"Cookie" : "_mc=m-1500860797760330344; hjstat_uv=3508143220436787490|679544; BDTUJIAID=270efab61a52b722c6be1f0aeed4f0a4; mop_uid=15105452190312868; Hm_lvt_478a545b1304d1c78ecf8fa7a9ef656f=1510623141; _ms=1511158095028008990"
        }
        
        response = requests.get(url, headers=headers)
        content = response.content
        strr = (str(content).rsplit(")")[0]).split("(")[1]
        json_list = json.loads(strr)
        self.article_dict = json_list['article']
        #print self.article_dict.keys()
        #return article_dict
    
    def getReplyDataList(self,pageNum):
        #baseUrl = 'http://comment.mop.com/mopcommentapi/dzh/replylist/api/v170828/replyat/offset/asc/1495930293000252398/'
        baseUrl = self.commentBaseUrl
        #pageNum = self.article_dict['replynum']/100 + 1
        url = baseUrl + str((pageNum-1)*100) +'/100'
        #url = 'http://comment.mop.com/mopcommentapi/dzh/replylist/api/v170828/replyat/offset/asc/1495930293000252398/1000/100'
        #print url        
        headers = {
            "Host" : "comment.mop.com",
            "Connection" : "keep-alive",
            "Accept" : "*/*",
            "Origin" : "http://dzh.mop.com",
            "X-Requested-With" : "XMLHttpRequest",
            "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Referer" : self.URL,
            "Accept-Encoding": "gzip, deflate, sdch",
            "Accept-Language": "zh-CN,zh;q=0.8",
            #"Cookie" : "_mc=m-1500860797760330344; hjstat_uv=3508143220436787490|679544; BDTUJIAID=270efab61a52b722c6be1f0aeed4f0a4; mop_uid=15105452190312868; Hm_lvt_478a545b1304d1c78ecf8fa7a9ef656f=1510623141; _ms=1510800282252181388; show20=1117"
        }
        
        response = requests.get(url, headers=headers)
        content = response.json()
        data_list = content['data']
        return data_list

        
#    def creatFile(self):
#        #如果标题不是为None，即成功获取到标题
#        title = self.article_dict['title']
#        if title is not None:
#            self.file = open(title + ".txt","w+")
#        else:
#            print u"没有取到帖子的title,请确认输入的参数是否正确！"

    #写入article开篇文章的内容
    def writeArticle(self):
        #向文件写入开头信息
        title = self.article_dict['title']
        username = self.article_dict['username']
        #rpt = Tool()
        article_content = self.tool.replace(self.article_dict['content'])
        ppublishtime = self.article_dict['publishtime']
        stamp = int(ppublishtime)/1000
        time_local = time.localtime(stamp)
        publishtime = time.strftime('%Y-%m-%d %H:%M:%S',time_local)
        print "writeArticle..."
        articl_title = "------------" + title + "------------" + "\n" + u"作者： " + username + u" 发表时间: " + publishtime + "\n" + article_content + "\n"
        self.file.write(articl_title)
    

    #取得回复列表中的当前作者的回复内容
    def getDataBody(self,list):
        
        contents = []
        for data in list:
            name = self.article_dict['username'].encode('utf-8')          
            #按照username来过滤回帖内容            
            if (data['username'] == name):
                #rpt = Tool()
                comment = self.tool.replace(data['body'])
                replytime_stamp = data['replytime']
                stamp = int(replytime_stamp)/1000
                time_local = time.localtime(stamp)
                replytime = time.strftime('%Y-%m-%d %H:%M:%S',time_local)
                self.lastfloor = int(data['floor'])
                #names1=['username','replytime','comment']                        
                content ="\n" + replytime + "," + comment + "\n"
                #print self.allFlag == 1
                if self.allFlag == 1:
                    contents.append(content.encode('utf-8'))
                elif self.allFlag == 0:
                    if (self.lastfloor > self.fileLastfloor):
                        contents.append(content.encode('utf-8'))
            else:
                pass
                
        return contents
   
    #写入回复列表中当前作者的回复内容
    def writeReplyData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            self.floor += 1
            #楼之间的分隔符
            floorLine = "\n" + str(self.floor) + u"楼 " + item[1:20] + "-----------------------------------------------------------------------------------------\n"           
            self.file.write(floorLine)
            self.file.write(item[21:])            

    def start(self):
        self.getArticleDict()
        if self.article_dict == None:
            print "article没有内容，请确认参数后重试!"
            return
        title = self.article_dict['title'].strip()
        pageNum = self.article_dict['replynum']/100 + 1
        #全部覆盖重写文件
        if self.allFlag == 1:
                    
            self.file = open(title + ".txt","w+")
            self.writeArticle()
            self.file.close()
            self.file = open(title + ".txt","a")
            try:
                print u"该帖子共有" + str(pageNum) + u"页"
                for i in range(1,int(pageNum)+1):
                    print u"正在写入第" + str(i) + u"页数据"
                    data_list = self.getReplyDataList(i)
                    contents = self.getDataBody(data_list)
                    self.writeReplyData(contents)
                print u"写入结尾行最新取得的楼层信息"
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                tail_msg = "\n" + "本次爬取帖子时间："+ current_time + " 取到的总楼层数和本次作者更新楼层为：" + "\n" + str(self.floor) + "&" + str(self.lastfloor)
                self.file.write(tail_msg.encode('utf-8'))
            #出现写入异常
            except IOError,e:
                print u"写入异常，原因" + e.message
            finally:
                print u"写入任务完成"
            self.file.close()
        #只更新后面的帖子
        elif self.allFlag == 0:
            rfile = open(title + ".txt","r")
            all_lines = rfile.readlines()           
            rfile.close()
            lastline = all_lines[-1]
            print lastline
            self.fileAmountfloor = int(lastline.split("&")[0])
            self.fileLastfloor = int(lastline.split("&")[1])
            self.floor = self.fileAmountfloor
            lastPageNum = self.fileLastfloor/100 + 1
            self.file = open(title + ".txt","a")
            try:
                print u"该帖子共有" + str(pageNum) + u"页，上次更新到第" + str(lastPageNum) + "页，第" + str(self.fileLastfloor) + "楼"
                for i in range(lastPageNum,int(pageNum)+1):
                    print u"正在写入第" + str(i) + u"页数据"
                    data_list = self.getReplyDataList(i)
                    contents = self.getDataBody(data_list)
                    self.writeReplyData(contents)
                print u"写入结尾行最新取得的楼层信息"
                current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                tail_msg = "\n" + "本次爬取帖子时间："+ current_time + " 取到的总楼层数和本次作者更新楼层为：" + "\n" + str(self.floor) + "&" + str(self.lastfloor)
                self.file.write(tail_msg.encode('utf-8'))
            #出现写入异常
            except IOError,e:
                print u"写入异常，原因" + e.message
            finally: 
                print u"写入任务完成"
            self.file.close()
                 


reload(sys)
sys.setdefaultencoding('utf8')


#Url,articleUrl,commentBaseUrl,allFlag

choice = raw_input(u"选择要抓取的猫扑帖子,输入1-我救了一个寡妇，却惹上了了恶鬼\n\
                   输入2-那些年，我在乡村的奇葩情事\n\
                   输入3-每日大盘评述\n")

allFlag = int(raw_input(u"从头开始重新爬取输入1，从文件上次更新处爬取输入0\n"))


if choice == '1':
    Url = 'http://dzh.mop.com/a/170528081133000252398.html'
    articleUrl = 'http://staticize.mop.com/subject/getArticleById?callback=jQuery18308948445668759089_1511158138413&id=50621250&type=dzh&_=1511158138628'
    commentBaseUrl = 'http://comment.mop.com/mopcommentapi/dzh/replylist/api/v170828/replyat/offset/asc/1495930293000252398/'
elif choice == '2':
    Url = 'http://dzh.mop.com/a/171110114839103505760.html'
    articleUrl = 'http://staticize.mop.com/subject/getArticleById?callback=jQuery183004722595994507417_1511443231277&id=51046379&type=dzh&_=1511443231412'
    commentBaseUrl = 'http://comment.mop.com/mopcommentapi/dzh/replylist/api/v170828/replyat/offset/asc/1510285719103505760/'
elif choice == '3':
    Url = 'http://dzh.mop.com/a/070118143620000560623.html'
    articleUrl = 'http://staticize.mop.com/subject/getArticleById?callback=jQuery18308730334619570397_1511443960791&id=7274201&type=dzh&_=1511443961128'
    commentBaseUrl = 'http://comment.mop.com/mopcommentapi/dzh/replylist/api/v170828/replyat/offset/asc/1169102180000560623/'
    

moper = Moper(Url,articleUrl,commentBaseUrl,allFlag)
moper.start()
