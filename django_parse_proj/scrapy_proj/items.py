"""this module contains scrapy items: Product"""
import scrapy


class Product(scrapy.Item):
    """Product from lordandtaylor site"""
    url = scrapy.Field()
    category = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    colors_and_sizes = scrapy.Field()
    images = scrapy.Field()
    description = scrapy.Field()
