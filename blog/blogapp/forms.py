from django import forms
from .models import Blogs  # Import your Blogs model

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blogs  # Specify the model class
        fields = ['blog']  # Specify the fields to include in the form
