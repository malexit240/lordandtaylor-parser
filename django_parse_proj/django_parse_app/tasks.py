"""this module contains celery tasks"""

from django_parse_proj.celery_app import app
import django_parse_app


@app.task
def save_product_to_db(products: list):
    """this task save products to db"""
    for product in products:
        p = django_parse_app.models.Product(url=product['url'],
                                            category=product['category'],
                                            price=product['price'],
                                            title=product['title'],
                                            colors=product['colors'],
                                            images=product['images'],
                                            description=product['description']
                                            )
        p.save()
