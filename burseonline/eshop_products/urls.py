from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import ProductsList, SearchProductsView, ProductsListByCategory\
    , products_categories_partial, upload_video, display_video, add_product_category, product_detail, add_comment

urlpatterns = [
    path('products', ProductsList.as_view()),
    path('products/<int:pk>', product_detail, name='product-detail'),
    path('products/add_category', add_product_category),
    path('products/<category_name>', ProductsListByCategory.as_view()),
    # path('products/<productId>/<name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products_categories_partial', products_categories_partial, name='products_categories_partial'),
    path('products/add_comment/<int:pk>', add_comment, name='prod-comment'),
    path('upload/', upload_video, name='upload'),
    path('videos/', display_video, name='videos')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)