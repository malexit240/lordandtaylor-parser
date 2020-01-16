from django_parse_proj.celery_app import app
#from .models import Product
from logging import log


@app.task
def save_product_to_db(products):
    log(20, products)
