from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product, ProductCategory
from ckeditor.fields import RichTextField
from eshop_news.models import Comment
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.pk}-{instance.pk}{ext}"
    return f"account/{final_name}"


class Answer(models.Model):
    user = models.ManyToManyField(User)
    body_text = RichTextField(default=None, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'پاسخ تیکت'
        verbose_name_plural = 'پاسخ های تیکت'


class Ticket(models.Model):
    headline = models.CharField(max_length=255)
    answers = models.ManyToManyField(Answer, null=True, blank=True)
    body_text = RichTextField(default=None, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'تیکت'
        verbose_name_plural = 'تیکت ها'


class Wallet(models.Model):
    title = models.CharField(max_length=1500, null=True, blank=True)
    money = models.IntegerField(verbose_name='قیمت', default=0, blank=True)

    class Meta:
        verbose_name = 'کیف پول'
        verbose_name_plural = 'کیف پول ها'

    def __str__(self):
        return str(self.title)


class Factor(models.Model):
    title = models.CharField(max_length=1500, null=True, blank=True)
    price = models.IntegerField(verbose_name='قیمت', default=0, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.CharField(max_length=1500, null=True, blank=True)

    class Meta:
        verbose_name = 'فاکتور'
        verbose_name_plural = 'فاکتور ها'

    def __str__(self):
        return str(self.pk)


class Question(models.Model):
    title = models.CharField(max_length=1500, null=True, blank=True)
    visit = models.IntegerField(verbose_name='بازدید', default=0, blank=True)
    body_text = RichTextField(default=None, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    answers = models.ManyToManyField(Answer, null=True, blank=True)
    category = models.ManyToManyField(ProductCategory, null=True, blank=True, verbose_name='دسته بندی')
    # rating = models.IntegerField(verbose_name='امتیاز', default=0, blank=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'سوال'
        verbose_name_plural = 'سوالات'


class ContactUs(models.Model):
    name = models.CharField(max_length=1500, null=True, blank=True, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=1500, null=True, blank=True, verbose_name="شماره موبایل")
    email = models.CharField(max_length=1500, null=True, blank=True, verbose_name="ایمیل")
    body_text = RichTextField(default=None, blank=True, null=True, verbose_name="متن")

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'ارتباط'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    wallet = models.ForeignKey(Wallet, null=True, blank=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1500, null=True, blank=True)
    skills = models.CharField(max_length=1500, null=True, blank=True)
    image = models.ImageField(upload_to=upload_image_path, default=None, null=True, blank=True)
    bought_products = models.ManyToManyField(Product, null=True, blank=True)
    tickets = models.ManyToManyField(Ticket, null=True, blank=True)
    factors = models.ManyToManyField(Factor, null=True, blank=True)
    questions = models.ManyToManyField(Question, null=True, blank=True)

    prof = models.BooleanField(default=False, verbose_name='استاد')
    vip = models.BooleanField(default=False, verbose_name='کاربر خاص')
    advisor = models.BooleanField(default=False, verbose_name='مشاور')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل ها'


# Create your models here.


