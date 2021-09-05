import itertools
from django.shortcuts import render

from eshop_products.models import Product
from eshop_products_category.models import MotherCategory
from eshop_news.models import Blog
from eshop_sliders.models import Slider
from eshop_setting.models import SiteSetting
from eshop_news.models import Blog
from django.contrib.auth.models import User
from eshop_account.models import Profile
from .models import WorkWithUs, AboutUs

from django.http.response import HttpResponse


from eshop_account.forms import ContactForm


# header code behind
def header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'category': MotherCategory.objects.all()
    }
    return render(request, 'shared/Header.html', context)


def home_header(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'category': MotherCategory.objects.all()
    }
    return render(request, 'shared/Home_header.html', context)


def main_menu(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'category': MotherCategory.objects.all()
    }
    return render(request, 'shared/main_menu.html', context)


def fixed_menu(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'category': MotherCategory.objects.all()
    }
    return render(request, 'shared/fixed_menu.html', context)


def top_slider(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'category': MotherCategory.objects.all()
    }
    return render(request, 'shared/top_slider.html', context)


def news_letter(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'category': MotherCategory.objects.all()
    }
    return render(request, 'shared/news_letter.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'category': MotherCategory.objects.all()
    }
    return render(request, 'shared/Footer.html', context)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


# code behind
def home_page(request):
    sliders = Slider.objects.all()
    most_visit_products = Product.objects.order_by('-visit_count').all()[:8]
    latest_products = Product.objects.order_by('-id').all()[:8]
    context = {
        'data': 'قروشگاه',
        'sliders': sliders,
        'most_visit': my_grouper(4, most_visit_products),
        'latest_products': my_grouper(4, latest_products),
        'category': MotherCategory.objects.all(),
        'blog': Blog.objects.all()
    }
    return render(request, 'index.html', context)


def about_page(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'text': AboutUs.objects.all()[0]
    }

    return render(request, 'about-us.html', context)


def contact_us(request):
    site_setting = SiteSetting.objects.first()
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('invalid input')
    context = {
        'setting': site_setting,
        'form': form
    }

    return render(request, 'contact-us.html', context)


def advisors(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }

    return render(request, 'advisors.html', context)


def word_with_us(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting,
        'text': WorkWithUs.objects.all()[0],
    }

    return render(request, 'work-with-us.html', context)


def masters(request):
    users = User.objects.all()
    masters_list = [user for user in users if user.profile.prof]
    site_setting = SiteSetting.objects.first()
    context = {
        'masters': masters_list,
        'setting': site_setting
    }

    return render(request, 'masters-archive.html', context)


def master_page(request, pk):
    users = User.objects.all()
    master = [user for user in users if user.pk == pk]
    context = {
        'master': master[0]
    }
    return render(request, 'mastar.html', context)

