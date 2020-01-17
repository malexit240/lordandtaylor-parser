"""this module contains websocket consumers"""

import json
import logging
import redis

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.conf import settings


class ProductConsumer(WebsocketConsumer):
    """Consumer for page with products"""

    def connect(self):
        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            'products', self.channel_name)

    def receive(self, text_data, bytes_data=None):
        if text_data == 'I am ready':  # start parsing lordandtaylor site if received some message
            redis.Redis(host='localhost', port=6379).lpush('landt:start_urls',
                                                           *settings.URLS_FOR_SCRAPING['lordandtaylor'])
            logging.log(logging.INFO, 'Start scraping')

    def send_update(self, event):
        """sends updated info to page"""
        product = {}
        product['url'] = event['url']
        product['category'] = event['category']
        product['price'] = event['price']
        product['title'] = event['title']
        product['colors'] = event['colors']
        product['images'] = event['images']
        product['description'] = event['description']

        logging.log(logging.INFO, 'send info')
        self.send(text_data=json.dumps(product))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'products', self.channel_name)
