# Generated by Django 3.1.5 on 2021-02-25 16:33

from django.db import migrations, models
import eshop_ad.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1500, null=True)),
                ('video', models.FileField(upload_to=eshop_ad.models.upload_image_path)),
            ],
        ),
    ]
