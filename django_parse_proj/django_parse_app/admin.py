from django.contrib import admin
from .models import Product

import django_parse_app.signal_handlers

admin.site.register(Product)
