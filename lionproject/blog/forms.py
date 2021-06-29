from django import forms
from django.db import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields =['title','writer','body','image']