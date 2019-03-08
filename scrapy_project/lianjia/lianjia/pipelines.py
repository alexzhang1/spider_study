# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb
import io
# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')


class FilePipeline(object):
    def process_item(self, item, spider):
        with io.open('lianjia.txt', 'a+', encoding='utf-8') as f:
            # f = open('lianjia.txt', 'w')
            seq_col = item.keys()
            print "colum:", seq_col
            city = item['city']  # 城市
            region = item['region']  # 行政区域
            href = item['href']  # 房源链接
            name = item['name']  # 房源名称
            style = item['style']  # 房源结构
            area = item['area']  # 小区
            orientation = item['orientation']  # 朝向
            decoration = item['decoration']  # 装修
            elevator = item['elevator']  # 电梯
            floor = item['floor']  # 楼层高度
            build_year = item['build_year']  # 建造时间
            sign_time = item['sign_time']  # 签约时间
            unit_price = item['unit_price']  # 每平米单价
            total_price = item['total_price']  # 总价
            fangchan_class = item['fangchan_class']  # 房产类型
            school = item['school']  # 周边学校
            subway = item['subway']   #周边地铁
            seq = item.values()
            list2 = []
            for line in seq:
                if isinstance(line, int):
                    tem = str(line)
                else:
                    tem = line
                list2.append(tem)
                # print type(list2)
            f.writelines(','.join(list2) + '\n')
        #f.close()
        return item

class MysqlPipeline(object):
    collection = 'cnblog'  # mongo数据库的collection名字，随便

    def __init__(self, mysql_hosts, mysql_user, mysql_password, mysql_port, mysql_db):
        self.mysql_hosts = mysql_hosts
        self.mysql_user = mysql_user
        self.mysql_password = mysql_password
        self.mysql_port = mysql_port
        self.mysql_db = mysql_db

    @classmethod
    def from_crawler(cls, crawler):
        '''
        scrapy为我们访问settings提供了这样的一个方法，这里，
        我们需要从settings.py文件中，取得数据库的URI和数据库名称
        '''

        return cls(
            mysql_hosts=crawler.settings.get('MYSQL_HOSTS'),
            mysql_user=crawler.settings.get('MYSQL_USER'),
            mysql_password = crawler.settings.get('MYSQL_PASSWORD'),
            mysql_port = crawler.settings.get('MYSQL_PORT'),
            mysql_db = crawler.settings.get('MYSQL_DB')
        )


    def open_spider(self, spider):  # 爬虫一旦开启，就会实现这个方法，连接到数据库
        # 打开数据库连接
        self.db = MySQLdb.connect(self.mysql_hosts, self.mysql_user, self.mysql_password, self.mysql_db, charset = "utf8")
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()


    #@classmethod
    def insert_dd_name(self, city, region, href, name, style, area, orientation, decoration, elevator, floor, build_year, sign_time, unit_price, total_price, fangchan_class, school, subway):
        # SQL 插入语句
        sql = "INSERT INTO lianjia_cj(city, region, href, name, style, area, orientation, decoration, elevator, floor, build_year, sign_time, unit_price, total_price, fangchan_class, school, subway) \
               VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s' )" % \
              (city, region, href, name, style, area, orientation, decoration, elevator, floor, build_year, sign_time,
               unit_price, total_price, fangchan_class, school, subway)
        try:
            # 执行sql语句
            print "do execute sql!"
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except Exception as e:
            print "insert_db failed:", e
            # 发生错误时回滚
            self.db.rollback()


        # 关闭数据库连接
        # self.db.close()

    #@classmethod
    # def select_name(self, name_id):
    #     sql = "select exists(select 1 from lianjia_cj whrere name_id = '%s' " % (name_id)
    #     try:
    #         # 执行sql语句
    #         self.cursor.execute(sql)
    #         # 提交到数据库执行
    #         self.db.commit()
    #     except:
    #         # 发生错误时回滚
    #         self.db.rollback()
    #
    #     # 关闭数据库连接
    #     # db.close()
    #     return self.cursor.fetchall()[0]



    def close_spider(self, spider):  # 爬虫一旦关闭，就会实现这个方法，关闭数据库连接
        self.db.close()


    def process_item(self, item, spider):
        '''
        每个实现保存的类里面必须都要有这个方法，且名字固定，用来具体实现怎么保存
        '''

        # name_id = item['name_id']
        # ret = Sql.select_name(name_id)
        # if ret[0] == 1:
        #     print('It is already exsit!')
        #     pass
        # else:
        #     xs_name = item['name']
        #     xs_author = item['author']
        #     novelurl = item['novelurl']
        #     serialstatus = item['serialstatus']
        #     serialnumber = item['serialnumber']
        #     category = item['category']
        #     name_id = item['name_id']
        #     Sql.insert_dd_name(xs_name, xs_author, category, name_id, novelurl, serialstatus, serialnumber)
        #     print('Beginning store novel name!')

        city = item['city']  # 城市
        region = item['region']  # 行政区域
        href = item['href']  # 房源链接
        name = item['name']  # 房源名称
        style = item['style']  # 房源结构
        area = item['area']  # 小区
        orientation = item['orientation']  # 朝向
        decoration = item['decoration']  # 装修
        elevator = item['elevator']  # 电梯
        floor = item['floor']  # 楼层高度
        build_year = item['build_year']  # 建造时间
        sign_time = item['sign_time']  # 签约时间
        unit_price = item['unit_price']  # 每平米单价
        total_price = item['total_price']  # 总价
        fangchan_class = item['fangchan_class']  # 房产类型
        school = item['school']  # 周边学校
        subway = item['subway']  # 周边地铁
        self.insert_dd_name(city, region, href, name, style, area, orientation, decoration, elevator, floor, build_year, sign_time, unit_price, total_price, fangchan_class, school, subway)
        print('Beginning store !')