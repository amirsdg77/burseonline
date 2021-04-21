from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, EditUserForm
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.http.response import HttpResponse


from eshop_account.forms import VideoForm, ProductForm
from eshop_setting.models import SiteSetting
from .models import Profile
from eshop_products.models import Product, Videos


# Create your views here
class PurchasedProductsList(ListView):
    model = User
    template_name = "account/purchased_product_list.html"
    paginate_by = 6


class PurchasedProduct(DetailView):
    model = Product
    template_name = "account/purchased_product.html"


class PurchasedProductVideo(DetailView):
    model = Videos
    template_name = "account/purchased_product_videos.html"


def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            login_form.add_error('user_name', 'کاربری با مشخصات وارد شده یافت نشد')

    context = {
        'login_form': login_form
    }
    return render(request, 'account/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)

    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        password = register_form.cleaned_data.get('password')
        email = register_form.cleaned_data.get('email')
        user = User.objects.create_user(username=user_name, email=email, password=password)
        profile = Profile(user=user)
        profile.save()

        return redirect('/login')

    context = {
        'register_form': register_form
    }
    return render(request, 'account/register.html', context)


def log_out(request):
    logout(request)
    return redirect('/login')


@login_required(login_url='/login')
def user_account_main_page(request):
    if request.user.has_perm('poll.change_poll'):
        return render(request, 'account/admin_account_main.html', {})
    else:

        return render(request, 'account/user_account_main.html', {'user': request.user})


@login_required(login_url='/login')
def edit_user_profile(request):
    user = request.user
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    if request.method == 'POST':
        edit_user_form = EditUserForm(request.POST or None, request.FILES or None)
        if edit_user_form.is_valid():
            first_name = edit_user_form.cleaned_data.get('first_name')
            last_name = edit_user_form.cleaned_data.get('last_name')
            image = edit_user_form.cleaned_data.get('image')
            bio = edit_user_form.cleaned_data.get('bio')

            user.profile.bio = bio
            user.profile.image = image
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            user.profile.save()
        else:
            return HttpResponse('invalid input')
    else:
        edit_user_form = EditUserForm

    context = {'edit_form': edit_user_form}

    return render(request, 'account/edit_account.html', context)


def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})


def admin_sidebar(request):
    return render(request, 'account/admin_sidebar.html', {})


def add_product(request):
    if request.method == 'POST':
        if not request.user.has_perm('poll.change_poll'):
            return HttpResponseForbidden('Nope!')
        else:
            product_form = ProductForm(request.POST, request.FILES)
            if product_form.is_valid():
                product_form.save()
                return redirect('/')
            return HttpResponse('Nope!')
    else:
        product_form = ProductForm()

    context = {
        'setting': SiteSetting,
        'product_form': product_form
    }

    return render(request, 'account/add_product_page.html', context)
