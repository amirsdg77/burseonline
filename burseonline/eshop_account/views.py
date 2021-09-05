from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, EditUserForm, ChangePasswordForm, TicketForm, QuestionForm, AnswerForm
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.http.response import HttpResponse
from passlib.hash import django_pbkdf2_sha256 as handler


from eshop_account.forms import VideoForm, ProductForm
from eshop_setting.models import SiteSetting
from .models import Profile, Ticket, Wallet, Question, Factor
from eshop_products.models import Product, Videos, ProductCategory
from eshop_products_category.models import MotherCategory


from zeep import Client


# Create your views here
class ForumView(ListView):
    model = Question
    template_name = "account/forum.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context.update({
            'categories': MotherCategory.objects.all()
        })
        return context


def forum(request, pk):
    question_list = [i for i in Question.objects.all() if i.category.all()[0].pk == pk]

    context = {
        'object_list': question_list,
        'categories': MotherCategory.objects.all()
    }

    return render(request, "account/forum.html", context)


def forum_question(request, pk):
    question = None
    for question in Question.objects.all():
        if question.pk == pk:
            question = question
            break
    form = AnswerForm(request.POST or None)
    context = {
        'question': question,
        'form': form,
        'categories': ProductCategory.objects.all
    }
    return render(request, "account/forum-question.html", context)


class PurchasedProductsList(ListView):
    model = User
    template_name = "account/dashboard/my-courses.html"
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
        profile.wallet = Wallet().save()
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
    # if request.user.has_perm('poll.change_poll'):
    #     return render(request, 'account/admin_account_main.html', {})
    # else:
    return render(request, 'account/dashboard/dashboard.html', {'user': request.user})


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
            skills = edit_user_form.cleaned_data.get('skills')

            user.profile.bio = bio
            user.profile.image = image
            user.profile.skills = skills
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            user.profile.save()
        else:
            return HttpResponse('invalid input')
    else:
        edit_user_form = EditUserForm(initial={'first_name': user.first_name,
                                               'last_name': user.last_name,
                                               'bio': user.profile.bio,
                                               'skills': user.profile.skills,
                                               'image': user.profile.image
                                               })

    context = {'edit_form': edit_user_form}

    return render(request, 'account/dashboard/edit_account.html', context)


@login_required(login_url='/login')
def change_password(request):
    user = request.user
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    if request.method == 'POST':
        change_password_form = ChangePasswordForm(request.POST or None)
        if change_password_form.is_valid():
            password = change_password_form.cleaned_data.get('password')
            re_password = change_password_form.cleaned_data.get('re_password')

            if password == re_password:
                user.password = handler.hash(password)
                user.save()

            else:
                return HttpResponse('no match!')

        else:
            return HttpResponse('invalid input')
    else:
        change_password_form = ChangePasswordForm

    context = {'edit_form': change_password_form}

    return render(request, 'account/dashboard/password_change.html', context)


@login_required(login_url='/login')
def user_sidebar(request):
    return render(request, 'account/user_sidebar.html', {})


@login_required(login_url='/login')
def admin_sidebar(request):
    return render(request, 'account/admin_sidebar.html', {})


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def support(request):
    user = request.user
    context = {
        'tickets': user.profile.tickets.all(),
        'user': user,
    }

    return render(request, 'account/dashboard/support.html', context)


@login_required(login_url='/login')
def view_ticket(request, pk):
    ticket = None
    for ticket in Ticket.objects.all():
        if ticket.pk == pk:
            ticket = ticket
            break

    context = {
        'ticket': ticket,
    }
    return render(request, 'account/dashboard/viewticket.html', context)


@login_required(login_url='/login')
def add_ticket(request):
    user = request.user
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST or None)
        if ticket_form.is_valid():
            headline = ticket_form.cleaned_data.get('headline')
            body = ticket_form.cleaned_data.get('body_text')

            ticket = Ticket()
            ticket.headline = headline
            ticket.body_text = body
            ticket.save()

            user.profile.tickets.add(ticket)
            user.save()
            user.profile.save()

        else:
            return HttpResponse('invalid input')
    else:
        ticket_form = TicketForm
    context = {
        'ticket_form': ticket_form,
        'user': request.user,
    }

    return render(request, 'account/dashboard/addticket.html', context)


@login_required(login_url='/login')
def consulting_request(request):
    context = {
        'user': request.user,
    }

    return render(request, 'account/dashboard/consulting-requests.html', context)


@login_required(login_url='/login')
def factor(request):
    context = {
        'user': request.user,
    }

    return render(request, 'account/dashboard/factor.html', context)


@login_required(login_url='/login')
def my_answers(request):
    context = {
        'user': request.user,
    }

    return render(request, 'account/dashboard/my-answers.html', context)


@login_required(login_url='/login')
def my_questions(request):
    context = {
        'user': request.user,
    }

    return render(request, 'account/dashboard/my-questions.html', context)


@login_required(login_url='/login')
def consultation_request(request):
    context = {
        'user': request.user,
    }

    return render(request, 'account/dashboard/submit-consultation-request.html', context)


@login_required(login_url='/login')
def q_a(request):
    site_setting = SiteSetting.objects.first()
    user = request.user
    if user is None:
        raise Http404('کاربر مورد نظر یافت نشد')
    if request.method == 'POST':
        question_form = QuestionForm(request.POST or None)
        if question_form.is_valid():
            # headline = question_form.cleaned_data.get('title')
            # body = question_form.cleaned_data.get('body_text')
            # category = question_form.cleaned_data.get('category')

            # question = Question()
            # question.title = headline
            # question.body_text = body
            # question.category.add(category)
            # question.save()

            question = question_form.save()

            user.profile.questions.add(question)
            user.profile.save()
            user.save()

        else:
            return HttpResponse('invalid input')
    else:
        question_form = QuestionForm

    context = {
        'setting': site_setting,
        'user': request.user,
        'question_form': question_form
    }

    return render(request, 'account/add-question.html', context)


@login_required(login_url='/login')
def answer(request, pk):
    question = None
    for question in Question.objects.all():
        if question.pk == pk:
            question = question
            break
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        ans = form.save()
        ans.user.add(request.user)
        ans.save()
        question.answers.add(ans)
        question.save()
    return redirect('/forum/' + str(pk))
