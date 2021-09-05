from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product, ProductCategory
from ckeditor.fields import RichTextField


class WorkWithUs(models.Model):
    body_text = RichTextField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'همکاری با ما'


class AboutUs(models.Model):
    body_text = RichTextField(default=None, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'درباره ما'
