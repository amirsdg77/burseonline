
from django.shortcuts import render

from .models import ProductCategory
from .forms import CategoryForm
from eshop_products.models import Product


def add_product_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()

    context = {
        'form': form
    }

    return render(request, '', context)

# Create your views here.
