from django import forms
from django.forms.fields import FilePathField
from django.forms.models import ModelForm
from blog.models import Author

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ("fullname", "bio", "profile_pic")