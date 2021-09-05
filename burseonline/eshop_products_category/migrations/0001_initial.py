# Generated by Django 3.2.5 on 2021-09-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MotherCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('name', models.CharField(max_length=150, verbose_name='عنوان در URL')),
            ],
            options={
                'verbose_name': 'دسته بندی مادر',
                'verbose_name_plural': 'دسته بندی های مادر',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='عنوان')),
                ('name', models.CharField(max_length=150, verbose_name='عنوان در URL')),
                ('mother_category', models.ManyToManyField(blank=True, default=None, null=True, to='eshop_products_category.MotherCategory')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
    ]