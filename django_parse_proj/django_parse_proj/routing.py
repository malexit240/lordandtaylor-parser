from django.urls import re_path

from channels.routing import ProtocolTypeRouter, URLRouter


from django_parse_app.consumers import ProductConsumer

app = ProtocolTypeRouter({
    'websocket': URLRouter([
        re_path(r'',
                ProductConsumer),
    ])
})
