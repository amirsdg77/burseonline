from django.urls import path

from .views import login_user, register, log_out, user_account_main_page, edit_user_profile, add_product\
    , PurchasedProductsList, PurchasedProduct, PurchasedProductVideo

urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register),
    path('log-out', log_out),
    path('user', user_account_main_page),
    path('user/edit', edit_user_profile),
    path('user/add_product', add_product),
    path('user/products', PurchasedProductsList.as_view()),
    path('user/products/<int:pk>', PurchasedProduct.as_view(), name="show-product"),
    path('user/products/product/<int:pk>', PurchasedProductVideo.as_view(), name="show-product-video"),
]
