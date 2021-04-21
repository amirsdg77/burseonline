import itertools

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.http.response import HttpResponse


from eshop_order.forms import UserNewOrderForm
from .models import Product, ProductGallery, Videos
from django.http import Http404
from eshop_products_category.models import ProductCategory

from eshop_account.forms import VideoForm
from eshop_setting.models import SiteSetting
from eshop_products_category.forms import CategoryForm
from eshop_news.forms import CommentForm

# Create your views here.


class ProductsList(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active_products()


def product_detail(request, pk):
    product = Product.objects.get_by_id(pk)

    product.visit_count += 1
    product.save()

    new_order_form = UserNewOrderForm(request.POST or None, initial={'product_id': pk})

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()

    grouped_related_products = my_grouper(3, related_products)

    galleries = ProductGallery.objects.filter(product_id=pk)

    grouped_galleries = list(my_grouper(3, galleries))

    form = CommentForm(request.POST or None)

    context = {
        'product': product,
        'galleries': grouped_galleries,
        'related_products': grouped_related_products,
        'new_order_form': new_order_form,
        'form': form
    }
    return render(request, 'products/product_detail.html', context)


def add_comment(request, pk):
    product = Product.objects.get_by_id(pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save()
        comment.user.add(request.user)
        comment.save()
        product.comment.add(comment)
        product.save()
    return redirect('/')


class ProductsListByCategory(ListView):
    model = Product
    template_name = 'products/products_list.html'
    paginate_by = 6

    # def get_queryset(self):
    #     print(self.kwargs)
    #     category_name = self.kwargs['category_name']
    #     category = ProductCategory.objects.filter(name__iexact=category_name).first()
    #     if category is None:
    #         raise Http404('صفحه ی مورد نظر یافت نشد')
    #     return Product.objects.get_products_by_category(category_name)


def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))


# def product_detail(request, *args, **kwargs):
#     selected_product_id = kwargs['productId']
#

#
#     if product is None or not product.active:
#         raise Http404('محصول مورد نظر یافت نشد')
#
#

#
#     context = {
#     }
#
#     return render(request, 'products/product_detail.html', context)


class SearchProductsView(ListView):
    template_name = 'products/products_list.html'
    paginate_by = 6

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Product.objects.search(query)

        return Product.objects.get_active_products()


def add_product_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CategoryForm()

    context = {
        'form': form
    }

    return render(request, 'products/add_product_category.html', context)


def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'products/products_categories_partial.html', context)


def upload_video(request):
    products = Product.objects.all()
    if request.method == 'POST':
        if not request.user.has_perm('poll.change_poll'):
            return HttpResponseForbidden('Nope!')
        else:
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                for product in products:
                    if form.cleaned_data.get('product_id') == product.id:
                        video = Videos(title=form.cleaned_data.get('title'),
                                       description=form.cleaned_data.get('description'),
                                       video=form.cleaned_data.get('video'))
                        video.save()
                        product.videos.add(video)
                        product.save()
                        return redirect('/')
            return HttpResponse('invalid input')

    else:
        form = VideoForm()

    context = {
        'setting': SiteSetting,
        'form': form
    }

    return render(request, 'account/product_video_upload.html', context)


def display_video(request, pk):
    print("hi")




