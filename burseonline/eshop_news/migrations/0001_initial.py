# Generated by Django 3.2.5 on 2021-09-05 12:07

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import eshop_news.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_products_category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('name', models.CharField(max_length=150, verbose_name='عنوان در URL')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', ckeditor.fields.RichTextField(blank=True, default=None, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'کامنت',
                'verbose_name_plural': 'کامنتها',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('title_image', models.ImageField(null=True, upload_to=eshop_news.models.upload_image_path)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('number_of_pingbacks', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='eshop_products_category.ProductCategory')),
                ('comments', models.ManyToManyField(blank=True, null=True, to='eshop_news.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('title_image', models.ImageField(null=True, upload_to=eshop_news.models.upload_image_path)),
                ('body_text', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('visit', models.IntegerField(blank=True, default=0, null=True)),
                ('rating', models.IntegerField(blank=True, default=0, null=True)),
                ('authors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('category', models.ManyToManyField(to='eshop_products_category.ProductCategory')),
                ('comments', models.ManyToManyField(blank=True, null=True, to='eshop_news.Comment')),
            ],
            options={
                'verbose_name': 'بلاگ',
                'verbose_name_plural': 'بلاگ ها',
            },
        ),
    ]
