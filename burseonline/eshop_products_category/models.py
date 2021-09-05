from django.db import models


# Create your models here.

class MotherCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name='عنوان در URL')

    class Meta:
        verbose_name = 'دسته بندی مادر'
        verbose_name_plural = 'دسته بندی های مادر'

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    mother_category = models.ManyToManyField(MotherCategory, default=None, blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name='عنوان در URL')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title
