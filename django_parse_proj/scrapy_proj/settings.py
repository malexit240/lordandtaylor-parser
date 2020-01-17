# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_proj project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapy_proj'

SPIDER_MODULES = ['scrapy_proj.spiders']
NEWSPIDER_MODULE = 'scrapy_proj.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SCHEDULER = "scrapy_redis.scheduler.Scheduler"

DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'

ITEM_PIPELINES = {
    'scrapy_proj.pipelines.ScrapyProjPipeline': 1,
    'scrapy_redis.pipelines.RedisPipeline': 2,
}


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16


# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
