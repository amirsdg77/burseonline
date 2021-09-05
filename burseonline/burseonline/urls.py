"""burseonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from burseonline import settings
from .view import home_page, header, footer, about_page, contact_us, home_header, main_menu, fixed_menu,\
    top_slider, news_letter, advisors, word_with_us, masters, master_page


urlpatterns = [
    path('', home_page),

    path('', include('eshop_account.urls')),
    path('', include('eshop_products.urls')),
    path('', include('eshop_contact.urls')),
    path('', include('eshop_order.urls')),
    path('', include('eshop_news.urls')),

    path('about-us', about_page),
    path('contact_us', contact_us),
    path('advisors', advisors),
    path('work_with_us', word_with_us),
    path('masters', masters),
    path('masters/<int:pk>', master_page, name='master-page'),

    path('header', header, name="header"),
    path('Home_header', home_header, name="Home_header"),
    path('main_menu', main_menu, name="main_menu"),
    path('fixed_menu', fixed_menu, name="fixed_menu"),
    path('top_slider', top_slider, name="top_slider"),
    path('news_letter', news_letter, name="news_letter"),
    path('footer', footer, name="footer"),

    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]


if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
