from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
import os



def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.headline}{ext}"
    return f"Blog/{final_name}"


class Comment(models.Model):
    user = models.ManyToManyField(User)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.pk)


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name='عنوان در URL')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Blog(models.Model):
    headline = models.CharField(max_length=255)
    title_image = models.ImageField(upload_to=upload_image_path, null=True)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    authors = models.ManyToManyField(User)
    number_of_pingbacks = models.IntegerField(default=0, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    comments = models.ManyToManyField(Comment,null=True, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.headline


class Education(models.Model):
    headline = models.CharField(max_length=255)
    title_image = models.ImageField(upload_to=upload_image_path, null=True)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    authors = models.ManyToManyField(User)
    number_of_pingbacks = models.IntegerField(default=0, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    comments = models.ManyToManyField(Comment,null=True, blank=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return str(self.headline)
