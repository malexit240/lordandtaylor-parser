from django.dispatch import receiver
from django.db.models.signals import post_save
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import Product


@receiver(post_save, sender=Product)
def send_update_info(instance: Product, **kwargs):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)('products',
                                    {
                                        'type': 'send.update',
                                        'url': instance.url,
                                        'category': instance.category,
                                        'price': instance.price,
                                        'title': instance.title,
                                        'colors': instance.colors,
                                        'images': instance.images,
                                        'description': instance.description,
                                    })
