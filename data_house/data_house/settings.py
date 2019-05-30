# -*- coding: utf-8 -*-

# Scrapy settings for data_house project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'data_house'

SPIDER_MODULES = ['data_house.spiders']
NEWSPIDER_MODULE = 'data_house.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'data_house (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3641.400 QQBrowser/10.4.3284.400'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ip = [
    '187.44.254.186:42258',
    '89.216.17.178:8080',
    '111.177.190.177:9999',
    '103.194.242.10:50407',
    '93.126.62.125:80',
    '111.177.171.39:9999',
    '167.99.75.117:8080',
    '47.94.169.110:80',
    '103.195.204.73:21776',
    '51.211.183.25:80',
    '1.215.70.130:44072',
    '60.13.42.241:9999',
    '36.89.39.11:3128',
    '124.105.29.184:3128',
    '182.52.87.190:46437',
    '134.119.205.243:1080',
    '202.125.94.139:1234',
    '212.90.168.150:52589',
    '41.72.207.45:8080',
    '31.170.63.84:80',
    '94.242.59.245:10010',
    '187.11.216.80:8080',
    '36.89.151.26:59760',
    '139.255.113.250:41677',
    '46.143.206.160:80',
    '113.200.214.164:9999',
    '168.0.8.225:8080',
    '195.225.49.131:58302',
    '103.81.13.137:57803',
    '83.213.14.157:54024',
]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'cookie': 'sessid=76383EE2-A33A-E932-9DF3-8162A1FF92BF; aQQ_ajkguid=5606EC48-68BF-04DA-2C9F-5F9908DC42E5; lps=http%3A%2F%2Fbeijing.anjuke.com%2Fsale%2F%3Fpi%3Dbaidu-cpc-bj-tyong2%26kwid%3D3317864933%26utm_term%3D%25e4%25ba%258c%25e6%2589%258b%25e6%2588%25bf%7Chttps%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.0f0000jeTx0mG_-ZT79dvO3Do_dk6Q_ox5ZC_2w59S5fKt2u579MfFqM6-N5bJCLM-q4HPlDHxIzuw1pZIRl_-K26EH2fxExKoOdUtiM4KCtF9AB2FR8jglFLgUQgW9e_a8k925tjpLHBUeymxBf6uHQqiIzgEuF_NtzXVFPWjIElBy5hY7HAJ54NIoEGaODIORiMXAVUmFWqgjZ2f.7R_NR2Ar5Od66EiO2OP4nkuTZp-DDUP7nZxAqBqM761s33TqSg5fYr1urEUsmhr5AEkvI5uE3tX8a9G4pauVQA75u9EusecT2XMj_L3I-S75H9vUnPSVHReiM-kl-9h9mzTUPB6.U1Yz0ZDqz5vlYtofVEe2doXO0A7bTgbqz5vlYtofVEe2doXO0A7bTgfqn6KspynqnfKY5UUSzVpLEsKGUHYznWR0u1dBugK1nfKdpHdBmy-bIfKspyfqnfKWpyfqn16d0AdY5HDsnHIxnH0krNtknjfYg1nvnjD0pvbqn0KzIjYYrjn0uy-b5HDYn1PxnWDsrH7xnH6dPWKxnW0vrHIxnW6vnj9xnW6drjNxnW6vn1-xnWm1PHKxnW6dnH-xnW6vnjm0mhbqnW0Yg1DdPfKVm1Y3nj64rj0dnj7xnH0snNtknW6zPHTdPjmvg100TgKGujYknsKkmv-b5HnsPsKzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjY3PHfYPHndnH00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdWUfKYIgnqnHTsrHcvn1D3rH64Pj6LrjDsrjb0ThNkIjYkPHRzPjRsrH0zPWnd0ZPGujY4nycznvm3nW0snjm3m1Rv0AP1UHYvwHb1nYPDwHckP19Df1cs0A7W5HD0TA3qn0KkUgfqn0KkUgnqn0KlIjYs0AdWgvuzUvYqn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7ts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqnHm0uhPdIjYs0AulpjYs0Au9IjYs0ZGsUZN15H00mywhUA7M5HD0UAuW5H00ULfqn0KETMKY5H0Wnan0mLFW5HDkn16z%26word%3D%25E4%25B8%2589%25E6%25B2%25B3%25E5%25B8%2582%25E4%25BA%258C%25E6%2589%258B%25E6%2588%25BF%26ck%3D8312.9.48.447.397.258.148.287%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D2.0.1.0.15.8271.0%26bc%3D110101; twe=2; _ga=GA1.2.1039474926.1552450942; _gid=GA1.2.190884799.1552450942; 58tj_uuid=f5132ff6-7a21-49d3-97f8-05ffbc1206f7; als=0; ajk_member_captcha=ab6b33e86c3e37788bf57e1a4c52ac4e; ctid=59; wmda_uuid=c2f744355371d64d9ce1975b46ba2f73; wmda_new_uuid=1; wmda_visited_projects=%3B6289197098934; browse_comm_ids=956555%7C637429%7C637434; propertys=qn1acy-poafwf_qma1v4-poafl6_qi1y6y-poaf5b_qlhzjd-poaetx_; wmda_session_id_6289197098934=1552459029729-51927fe2-609b-5a6b; init_refer=; new_uv=3; new_session=0; __xsptplusUT_8=1; ajk_member_id=155291370; ajk_member_name=U15524611600924; ajk_member_key=74a318c7c35fbee4c2a0de328918be7d; ajk_member_time=1583997120; aQQ_ajkauthinfos=0bX6CjNXNEtZArFUlDxc%2FSv6ZJdKAJFSuTiyx6xNpMNudiJasIRMZ0sqm5JnU%2FjPlO%2FAD9eeo6PyHjoGbH38AUovx1o; lui=155291370%3A1; __xsptplus8=8.5.1552459030.1552461161.12%232%7Cwww.baidu.com%7C%7C%7C%25E4%25B8%2589%25E6%25B2%25B3%25E5%25B8%2582%25E4%25BA%258C%25E6%2589%258B%25E6%2588%25BF%7C%23%23zxp70VEfSnWv1AEl3oNYJW-qBLzNrFQ4%23',
    'Referer': 'beijing.anjuke.com',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'data_house.middlewares.DataHouseSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'data_house.middlewares.DataHouseDownloaderMiddleware': 543,
    'data_house.middlewares.MyproxiesSpiderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'data_house.pipelines.DataHousePipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

LOG_FILE = 'anjuke.log'
LOG_ENABLE = True
LOG_ENCODING = 'utf-8'
LOG_LEVEL = 'DEBUG'

HTTPERROR_ALLOWED_CODES = [301, 302]
RETRY_HTTP_CODES = [301, 302]
