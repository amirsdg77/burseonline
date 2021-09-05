# Generated by Django 3.2.5 on 2021-09-05 12:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', ckeditor.fields.RichTextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'درباره ما',
            },
        ),
        migrations.CreateModel(
            name='WorkWithUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body_text', ckeditor.fields.RichTextField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'همکاری با ما',
            },
        ),
    ]