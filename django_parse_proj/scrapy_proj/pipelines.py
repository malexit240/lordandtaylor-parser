# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from django_parse_app.tasks import save_product_to_db


def save_products(products: list):
    jsonable_products = []
    for product in products:
        p = {
            'url': product['url'],
            'category ': product['category'],
            'price ': product['price'],
            'title ': product['title'],
            'colors ': json.dumps(product['colors_and_sizes']),
            'images ': json.dumps(product['images']),
            'description ': product['description']
        }
        jsonable_products.append(p)
    save_product_to_db.delay(jsonable_products)
    # send to celery


class ScrapyProjPipeline(object):

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.products = []

    def process_item(self, item, spider):
        self.products.append(item)

        if len(self.products) >= 1:  # ======CHANGEME========
            save_products(self.products)
            self.products.clear()

        return item
