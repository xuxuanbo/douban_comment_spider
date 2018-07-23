# -*- coding: utf-8 -*-

# Scrapy settings for doubancomment project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'doubancomment'

SPIDER_MODULES = ['doubancomment.spiders']
NEWSPIDER_MODULE = 'doubancomment.spiders'
USER_AGENT ="Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"
# COOKIES = {'ll':	"\"118284\"",
# 'bid':	"_rlToGT79Io",
# '__utma':	"30149280.1865417050.1503538177.1515479661.1515482835.47",
# '__utmz':	"30149280.1515471929.45.26.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/popup/login",
# 'ue':	"\"747561582@qq.com\"",
# '__utmv':	"30149280.9174",
# '_vwo_uuid_v2' :"1E3D217CC82F9CDBC96C1A952D54F885|11fcbef4c29b73b9ed83989cfd754468",
# 'ps':	"y",
# 'ct':	"y",
# 'push_noty_num':	"0",
# 'push_doumail_num':	"0",
# 'ap':	"1",
# '__ads_session	':"2heFv5JxCAntZS+HJgA=",
# '__utmc	':"30149280",
# '__utmb':	"30149280.2.10.1515482835",
# }

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'doubancomment (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 2.5
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_DEBUG=True
COOKIES_ENABLED = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'doubancomment.middlewares.DoubancommentSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'doubancomment.middlewares.PhantomJSMiddleware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'doubancomment.pipelines.DoubancommentPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
