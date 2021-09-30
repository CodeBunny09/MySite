from django import forms
from .models import Catagory, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'catagory', 'tags']