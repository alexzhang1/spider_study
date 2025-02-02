# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import sys


#处理页面标签类
class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()
 
#百度贴吧爬虫类
class BDTB:
 
    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ,floorTag):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)
        self.tool = Tool()
        #全局file变量，文件写入操作对象
        self.file = None
        #楼层标号，初始为1
        self.floor = 1
        #默认的标题，如果没有成功获取到标题的话则会用这个标题
        self.defaultTitle = u"百度贴吧"
        #是否写入楼分隔符的标记
        self.floorTag = floorTag
 
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
            #print url
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            #print response.read()
            #return response.read().decode('utf-8')
            return response.read()
        except urllib2.URLError, e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败,错误原因",e.reason
                return None

    #获取帖子标题
    def getTitle(self,page):
        #page = self.getPage(1)
        #print page
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>',re.S)
        result = re.search(pattern,page)
        #print result
        if result:
            #print result.group(1)  #测试输出
            return result.group(1).decode("utf-8").strip()
        else:
            return None

    #获取帖子一共有多少页
    def getPageNum(self,page):
        page = self.getPage(1)
        pattern = re.compile('回复贴，共<span.*?>(.*?)</span>',re.S)
        #pattern = re.compile('回复贴，共<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern,page)
        if result:
            print result.group(1)  #测试输出
            return result.group(1).strip()
        else:
            #print "none"
            return None

    #获取每一层楼的内容,传入页面内容
    def getContent(self,page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>',re.S)
        items = re.findall(pattern,page)
        contents = []
        #floor = 1
        for item in items:
            #print item
            #print floor,u"楼------------------------------------------------------------------------------------------------------------------------------------\n"
            #print self.tool.replace(item)
            content = "\n"+self.tool.replace(item)+"\n"
            contents.append(content.encode('utf-8'))
        return contents
    
    def setFileTitle(self,title):
        #如果标题不是为None，即成功获取到标题
        #title = 
        if title is not None:
            self.file = open(title + ".txt","w+")
        else:
            self.file = open(self.defaultTitle + ".txt","w+")

    def writeData(self,contents):
        #向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == '1':
                #楼之间的分隔符
                floorLine = "\n" + str(self.floor) + u"-----------------------------------------------------------------------------------------\n"
                self.file.write(floorLine)
            self.file.write(item)
            self.floor += 1    

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL已失效，请重试"
            return
        try:
            print u"该帖子共有" + str(pageNum) + u"页"
            for i in range(1,int(pageNum)+1):
                print u"正在写入第" + str(i) + u"页数据"
                #print "writing:" + str(i)
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeData(contents)
                #print "writepage:" + str(i) 
        #出现写入异常
        except IOError,e:
            print u"写入异常，原因" + e.message
            print "error!" + e.message
        finally:
            #print "finally!"
            print u"写入任务完成"
        self.file.close()



reload(sys)
sys.setdefaultencoding('utf8')
#print u"请输入帖子代号"
#baseURL = 'http://tieba.baidu.com/p/' + str(raw_input(u'http://tieba.baidu.com/p/'))
baseURL = 'http://tieba.baidu.com/p/3138733512'
#seeLZ = raw_input(u"是否只获取楼主发言，是输入1，否输入0\n")
#floorTag = raw_input(u"是否写入楼层信息，是输入1，否输入0\n")
#bdtb = BDTB(baseURL,seeLZ,floorTag)

bdtb = BDTB(baseURL,1,1)
page = bdtb.getPage(1)
pagenum = bdtb.getPageNum(page)
#bdtb.getTitle(bdtb.getPage(1))
#bdtb.start()



#baseURL = 'http://tieba.baidu.com/p/3138733512'
#bdtb = BDTB(baseURL,1,1)
##bdtb.getTitle()
#page = bdtb.getPage(1)
#bdtb.getContent(page)
