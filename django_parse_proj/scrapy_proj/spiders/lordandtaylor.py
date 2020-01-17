"""this module contains scrapy spider for parsing lordandtaylor.com"""

import scrapy
from scrapy.http import Response, Request
from scrapy_proj.items import Product
import json
from scrapy_redis.spiders import RedisSpider


def get_image_urls(product: dict):
    """returns list of urls"""
    images_ends = product['media']['images'] + [color['colorize_image_url']
                                                for color in product['colors']['colors']
                                                if not color['is_soldout']]

    return ['https://s7d9.scene7.com/is/image/LordandTaylor/' + code for code in images_ends]


def get_element_by_id(elements: dict, id: int):
    """returns element(color or size) by id"""
    element = [element
               for element in elements
               if element['id'] == id]

    if element:
        return element[0]


def get_colors_and_sizes(product: dict):
    """returns a complex dict with available colors and sizes"""

    colors = product['colors']['colors']
    sizes = product['sizes']['sizes']

    result = {color['label']: []
              for color in colors
              if not color['is_soldout']}

    for skus in product['skus']['skus']:
        if skus['status_alias'] == 'available':
            color = get_element_by_id(colors, skus['color_id'])
            size = get_element_by_id(sizes, skus['size_id'])
            result[color['label']].append(size['value'])

    return result


def parse_details(data: dict):
    """returns data(colors, sizes and image urls) from special json data"""
    data = data['ProductDetails']['main_products'][0]

    return {
        'colors': get_colors_and_sizes(data),
        'images': get_image_urls(data),
    }


class LordAndTaylorSpider(RedisSpider):
    """this spider parses lordandtaylor site

    parse starts from category pages and scrape all products from all pages in this categories.
    """

    name = 'landt'

    def parse_product(self, response: Response):
        """parses product info on product page"""

        details = parse_details(json.loads(response.xpath(
            '//div[contains(@class,"framework-component")]/script/text()').extract_first()))

        item = Product()
        item['url'] = response.url
        item['category'] = response.meta['category']
        item['price'] = response.xpath(
            '//span[@itemprop="price"]/@content | //span[contains(@itemprop, "lowPrice")]/@content').extract_first()
        item['title'] = response.xpath(
            '//a[@itemprop="name"]/text()').extract_first()
        item['colors_and_sizes'] = details['colors']
        item['images'] = details['images']
        item['description'] = ''.join(response.xpath(
            '//div[contains(@itemprop,"description")]//text()').extract()).strip().replace('\n', '').replace('\r', '')

        return item

    def parse_page_with_products(self, response: Response):
        """sends requests by product pages"""

        product_links = response.xpath(
            '//div[contains(@id,"product")]/@data-url').extract()[:10]  # ======DELETEME======

        for link in product_links:
            yield Request(link, self.parse_product, meta=response.meta)

    def parse(self, response: Response):
        """sends requests by pagination"""

        category = response.xpath('//h1/span/text()').extract_first()
        response.meta['category'] = category

        for _ in self.parse_page_with_products(response):
            yield _

        for page_url in response.xpath('//div[contains(@id,"pc-bottom")]/ol//li[contains(@class,"page-number")]/a/@href').extract():
            yield Request('https://www.lordandtaylor.com/' + page_url, self.parse_page_with_products,
                          meta={'category': category},)
