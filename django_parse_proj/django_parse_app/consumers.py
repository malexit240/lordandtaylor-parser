from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
import redis


class ProductConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            'products', self.channel_name)

    def receive(self, text_data, bytes_data=None):
        if text_data == 'I am ready':
            print('ready!')
            redis.Redis(host='localhost', port=6379).lpush('landt:start_urls',
                                                           'https://www.lordandtaylor.com/Men/Clothing/Activewear/shop/_/N-4ztez6/Ne-6ja3o7')

    def send_update(self, event):
        print(event)
        obj_to_send = {}
        obj_to_send['url'] = event['url']
        obj_to_send['category'] = event['category']
        obj_to_send['price'] = event['price']
        obj_to_send['title'] = event['title']
        obj_to_send['colors'] = event['colors']
        obj_to_send['images'] = event['images']
        obj_to_send['description'] = event['description']

        self.send(text_data=json.dumps(obj_to_send))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'products', self.channel_name)
