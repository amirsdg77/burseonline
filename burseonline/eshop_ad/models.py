from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product
from eshop_news.models import Comment
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{instance.pk}{ext}"
    return f"ad/{final_name}"


class Advertisement(models.Model):
    title = models.CharField(max_length=1500, null=True)
    video = models.FileField(upload_to=upload_image_path)

    def __str__(self):
        return self.title