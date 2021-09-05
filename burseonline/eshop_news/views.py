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


class LatestNews(ListView):
    model = Blog
    template_name = "blog.html"
    paginate_by = 9


class SearchBlogView(ListView):
    template_name = "blog.html"
    paginate_by = 9

    def get_queryset(self):
        request = self.request
        print(request.GET)
        query = request.GET.get('q')
        if query is not None:
            return Blog.objects.search(query)

        return Blog.objects.all()


def blog_page(request, pk):
    blog = None
    for bl in Blog.objects.all():
        if bl.pk == pk:
            blog = bl
            blog.visit += 1
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




