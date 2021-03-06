# Generated by Django 3.2.5 on 2021-09-05 12:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import eshop_products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eshop_products_category', '0001_initial'),
        ('eshop_news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('title_image', models.ImageField(null=True, upload_to=eshop_products.models.upload_image_path)),
                ('price', models.IntegerField(blank=True, default=0, verbose_name='قیمت')),
                ('discount_price', models.IntegerField(blank=True, default=0, verbose_name='تخفیف')),
                ('teacher', models.CharField(default=None, max_length=150, verbose_name='استاد')),
                ('skill', models.CharField(default=None, max_length=150, null=True, verbose_name='مهارت')),
                ('video', models.FileField(blank=True, null=True, upload_to=eshop_products.models.upload_image_path, verbose_name='ویدیو ی معرفی')),
                ('active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('visit_count', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
                ('categories', models.ManyToManyField(blank=True, to='eshop_products_category.ProductCategory', verbose_name='دسته بندی ها')),
                ('comment', models.ManyToManyField(blank=True, null=True, to='eshop_news.Comment')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number', models.IntegerField(blank=True, default=0, verbose_name='شماره ویدیو')),
                ('time', models.TimeField(default=None)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('video', models.FileField(upload_to=eshop_products.models.upload_image_path)),
            ],
            options={
                'verbose_name': 'ویدیو محصول',
                'verbose_name_plural': 'ویدیوهای محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to=eshop_products.models.upload_gallery_image_path, verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر',
                'verbose_name_plural': 'تصاویر',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='videos',
            field=models.ManyToManyField(blank=True, null=True, to='eshop_products.Videos'),
        ),
    ]
