# Generated by Django 3.1.5 on 2021-02-01 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
