# -*- coding: utf-8 -*-

# Scrapy settings for lianjia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lianjia'

SPIDER_MODULES = ['lianjia.spiders']
NEWSPIDER_MODULE = 'lianjia.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lianjia (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]

# PROXIES = ['http://183.207.95.27:80', 'http://111.6.100.99:80', 'http://122.72.99.103:80',
#            'http://106.46.132.2:80', 'http://112.16.4.99:81', 'http://123.58.166.113:9000',
#            'http://118.178.124.33:3128', 'http://116.62.11.138:3128', 'http://121.42.176.133:3128',
#            'http://111.13.2.131:80', 'http://111.13.7.117:80', 'http://121.248.112.20:3128',
#            'http://112.5.56.108:3128', 'http://42.51.26.79:3128', 'http://183.232.65.201:3128',
#            'http://118.190.14.150:3128', 'http://123.57.221.41:3128', 'http://183.232.65.203:3128',
#            'http://166.111.77.32:3128', 'http://42.202.130.246:3128', 'http://122.228.25.97:8101',
#            'http://61.136.163.245:3128', 'http://121.40.23.227:3128', 'http://123.96.6.216:808',
#            'http://59.61.72.202:8080', 'http://114.141.166.242:80', 'http://61.136.163.246:3128',
#            'http://60.31.239.166:3128', 'http://114.55.31.115:3128', 'http://202.85.213.220:3128']

# PROXIES = ['https://101.132.122.230:3128', 'https://115.233.209.134:3128', 'https://118.31.56.49:3128', 'https://113.87.161.115:8088', 'http://114.115.182.59:3128', 'https://125.66.165.155:53281', 'https://114.226.135.208:6666', 'https://183.13.169.142:9797', 'https://112.250.65.222:53281', 'https://117.63.78.110:6666', 'https://14.117.208.21:9797', 'https://122.72.18.34:80', 'https://211.80.62.74:1080', 'https://117.63.78.189:6666', 'https://1.196.161.172:9999', 'https://114.228.75.254:6666', 'https://61.144.16.58:9797', 'https://101.37.79.125:3128', 'https://116.226.118.248:9000', 'https://180.173.64.57:9797', 'https://120.78.78.141:8888', 'https://121.231.154.142:6666', 'https://222.185.137.138:6666', 'https://14.117.210.106:9797', 'https://222.245.132.219:80', 'https://118.81.69.58:9797', 'https://117.86.207.121:18118', 'https://120.24.62.4:9999', 'https://113.76.96.237:9797', 'https://121.201.33.100:16448', 'https://163.125.195.146:9797', 'https://183.30.201.113:9797', 'https://118.212.137.135:31288', 'https://182.88.199.69:9797', 'https://163.125.71.53:9999', 'https://163.125.71.49:9999', 'http://112.115.57.20:3128', 'https://27.19.69.88:8123', 'https://114.228.73.100:6666', 'https://121.231.168.150:6666', 'https://121.231.32.171:6666', 'https://112.95.206.195:8888', 'https://219.131.241.127:9797', 'https://222.185.23.228:6666', 'https://114.113.126.83:80', 'https://175.25.26.117:3128', 'https://112.74.176.103:3128', 'https://114.226.135.83:6666', 'https://119.48.175.99:9999', 'https://117.63.78.239:6666', 'https://14.153.54.122:3128', 'https://222.185.137.149:6666', 'https://171.13.94.231:9797', 'https://121.231.226.131:6666', 'https://222.186.12.102:57624', 'https://222.185.22.111:6666', 'https://182.88.189.81:9797', 'https://219.219.244.79:61202', 'https://125.118.66.17:9999', 'https://123.13.247.120:9999', 'http://110.185.227.236:9999', 'https://115.229.80.189:9000', 'https://222.185.137.102:6666', 'https://114.228.73.242:6666', 'https://115.229.114.235:9000', 'https://222.185.160.43:6666', 'https://113.65.127.136:9999', 'https://183.51.191.49:9999', 'https://114.228.75.188:6666', 'https://114.226.65.6:6666', 'https://223.243.209.114:63909', 'https://112.95.21.215:9999', 'https://27.46.49.145:9797', 'https://182.111.50.41:3128', 'https://222.185.23.146:6666', 'https://27.44.160.107:9797', 'https://114.228.73.9:6666', 'https://222.185.23.192:6666', 'https://114.226.135.153:6666', 'https://182.18.13.149:53281', 'https://163.125.70.11:8888', 'https://114.226.105.166:6666', 'https://114.228.75.95:6666', 'https://114.226.65.128:6666', 'https://113.78.64.145:9797', 'https://183.33.192.70:9797', 'https://114.228.73.206:6666', 'https://121.231.155.14:6666', 'http://222.186.12.99:52311', 'https://27.46.20.62:888', 'https://222.186.45.127:55336', 'https://117.66.167.176:8118', 'https://222.185.137.85:6666', 'https://14.153.53.147:3128', 'https://123.138.89.133:9999', 'https://119.122.2.250:9000', 'https://222.185.160.194:6666', 'https://113.78.255.203:9000', 'https://27.44.163.21:9999', 'https://121.231.155.179:6666', 'https://27.44.164.66:9999', 'https://222.185.23.3:6666', 'https://163.125.194.29:9797', 'https://183.14.25.26:9000', 'https://58.251.230.41:9797', 'https://114.226.105.2:6666', 'https://113.116.147.224:9000', 'https://121.231.155.6:6666', 'https://222.186.45.125:65309', 'https://113.65.127.191:9999', 'https://171.37.141.63:9797', 'https://27.37.47.117:9797', 'https://114.226.65.182:6666', 'https://144.255.160.39:6666', 'https://114.228.74.228:6666', 'https://115.213.201.153:8070', 'https://106.110.35.149:40662', 'https://182.246.232.168:25089', 'https://115.198.34.15:6666', 'https://175.148.74.12:1133', 'https://114.231.66.191:18118', 'https://14.118.255.25:6666', 'https://222.185.23.130:6666', 'https://14.118.253.53:6666', 'https://58.214.51.100:8070', 'https://58.214.51.151:8070', 'https://220.191.15.51:6666', 'https://115.198.36.79:6666', 'https://49.70.24.117:61234', 'https://144.255.104.145:6666', 'https://125.122.119.124:6666', 'https://14.118.252.195:6666', 'https://60.176.235.207:6666', 'https://116.115.209.141:36198', 'https://222.185.160.52:6666', 'https://121.231.154.222:6666', 'https://116.115.208.12:22940', 'https://121.231.154.199:6666', 'https://115.198.38.165:6666', 'https://14.118.252.239:6666', 'https://182.246.247.51:40267', 'https://125.118.149.233:6666', 'https://14.118.255.198:6666', 'https://222.185.137.14:6666', 'https://121.231.155.106:6666', 'https://125.118.247.175:6666', 'https://114.228.75.90:6666', 'http://222.171.83.213:63000', 'https://115.198.32.171:6666', 'https://121.31.197.111:8123', 'https://222.185.160.239:6666', 'https://114.225.169.39:53128', 'https://114.228.75.101:6666', 'https://223.241.79.97:18118', 'https://122.194.211.36:41546', 'https://222.185.23.75:6666', 'https://121.31.163.83:8123', 'https://223.145.231.147:6666', 'https://175.11.215.132:808', 'https://14.118.252.96:6666', 'https://125.118.148.21:6666', 'https://222.185.23.149:6666', 'https://125.120.11.219:6666', 'https://14.118.252.100:6666', 'https://175.42.68.158:30089', 'https://125.120.9.176:6666', 'https://14.118.254.52:6666', 'https://125.122.171.226:6666', 'https://222.185.137.110:6666', 'https://114.226.128.135:6666', 'https://113.105.203.150:3128', 'https://125.120.9.217:6666', 'https://121.31.103.110:8123', 'https://14.118.253.28:6666', 'https://118.122.92.252:37901', 'https://114.228.75.246:6666', 'https://14.118.255.143:6666', 'https://222.185.22.71:6666', 'https://111.183.231.46:41749', 'https://223.145.228.155:6666', 'https://114.237.55.3:44754', 'https://119.186.19.207:61234', 'https://14.118.254.220:6666', 'https://183.143.60.161:61234', 'https://182.45.177.34:6666', 'https://114.237.3.182:61234', 'https://222.241.103.191:38185', 'https://114.226.135.37:6666', 'https://114.228.75.65:6666', 'https://183.159.84.172:18118', 'https://14.118.254.106:6666', 'https://114.228.73.82:6666', 'https://121.231.155.2:6666', 'https://223.145.231.53:6666', 'https://125.120.203.91:6666', 'https://125.120.202.64:6666', 'https://59.38.241.59:61234', 'https://175.146.96.42:8010', 'https://222.185.22.80:6666', 'https://171.39.73.48:8123', 'https://114.226.135.177:6666', 'https://115.49.125.254:42234', 'https://182.122.42.224:44391', 'https://114.231.66.218:18118', 'https://114.237.57.246:45156', 'https://119.10.67.144:808', 'https://121.31.100.50:8123', 'https://121.231.226.156:6666', 'https://14.118.253.181:6666', 'https://113.121.241.125:61234', 'https://220.191.102.8:6666', 'https://114.226.105.84:6666', 'https://219.129.169.246:63000', 'https://121.237.140.149:35412', 'https://42.202.41.165:30915', 'https://59.32.37.63:61234', 'https://114.228.73.253:6666', 'https://220.184.215.248:6666', 'https://14.118.252.83:6666']
PROXIES = ['http://222.185.22.210:6666', 'http://121.41.171.223:3128']

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
RETRY_TIMES = 5
DUPEFILTER_DEBUG = True
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection':'keep-alive'
}


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lianjia.middlewares.LianjiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lianjia.middlewares.LianjiaDownloaderMiddleware': 543,
#}

DOWNLOADER_MIDDLEWARES = {
    'lianjia.middlewares.MyUserAgentMiddleware': 500,
    'lianjia.middlewares.ProxyMiddleware': 600,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'lianjia.pipelines.LianjiaPipeline': 300,
#}


ITEM_PIPELINES = {
    'lianjia.pipelines.FilePipeline': 300,
    'lianjia.pipelines.MysqlPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MYSQL_HOSTS = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_PORT = '3306'
MYSQL_DB = 'testdb'
