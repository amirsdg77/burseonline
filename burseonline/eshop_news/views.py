from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from eshop_account.models import Profile

from .forms import BlogForm, CommentForm, CategoryForm, EducationForm
from eshop_setting.models import SiteSetting
from .models import Blog, Comment, Education


class EducationView(ListView):
    model = Education
    template_name = "education.html"
    paginate_by = 10


def education_page(request, pk):
    blog = None
    for blog in Education.objects.all():
        if blog.pk == pk:
            blog = blog
            break
    form = CommentForm(request.POST or None)
    context = {
        'education': blog,
        'form': form
    }
    return render(request, 'education_page.html', context)


def add_edu(request):
    current_user = request.user
    if request.method == 'POST':
        form = EducationForm(request.POST, request.POST, request.POST)
        if form.is_valid():
            blog = form.save()
            blog.authors.add(current_user)
            blog.save()
            return redirect('/education')
    else:
        form = BlogForm()

    context = {
        'form': form
    }

    return render(request, 'add_blog.html', context)


def add_edu_comment(request, pk):
    blog = None
    for blog in Education.objects.all():
        if blog.pk == pk:
            blog = blog
            break
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save()
        comment.user.add(request.user)
        comment.save()
        blog.comments.add(comment)
        blog.save()
    return redirect('/education/' + str(pk))


class LatestNews(ListView):
    model = Blog
    template_name = "blog.html"
    paginate_by = 10


def blog_page(request, pk):
    blog = None
    for blog in Blog.objects.all():
        if blog.pk == pk:
            blog = blog
            break
    form = CommentForm(request.POST or None)
    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'blog_page.html', context)


def add_comment(request, pk):
    blog = None
    for blog in Blog.objects.all():
        if blog.pk == pk:
            blog = blog
            break
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save()
        comment.user.add(request.user)
        comment.save()
        blog.comments.add(comment)
        blog.save()
    return redirect('/blog/'+str(pk))


def news(request):
    site_setting = SiteSetting.objects.first()
    context = {
        'setting': site_setting
    }

    return render(request, 'education.html', context)


def add_blog_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else:
        form = CategoryForm()

    context = {
        'form': form
    }

    return render(request, 'add_blog_category.html', context)


def add_blog(request):
    current_user = request.user
    if request.method == 'POST':
        form = BlogForm(request.POST, request.POST, request.POST)
        if form.is_valid():
            blog = form.save()
            blog.authors.add(current_user)
            blog.save()
            return redirect('/blog')
    else:
        form = BlogForm()

    context = {
        'form': form
    }

    return render(request, 'add_blog.html', context)




