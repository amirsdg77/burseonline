from django import forms
from django.core import validators
from .models import Blog, Comment, Category, Education


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('headline', 'body_text', 'category')


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('headline', 'body_text', 'category')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body_text',)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'name')

