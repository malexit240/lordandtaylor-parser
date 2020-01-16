from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse


class Index(TemplateView):
    template_name = "django_parse_app/page.html"
