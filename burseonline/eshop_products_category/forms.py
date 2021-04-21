from django import forms
from django.contrib.auth.models import User
from django.core import validators
from .models import ProductCategory


class CategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('title', 'name')
