from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment
from taggit.forms import TagWidget  # Import the TagWidget for better tag input handling


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    # Optional: You can define widgets for specific fields (e.g., using TagWidget for 'tags')
    widgets = {
        'tags': TagWidget()  # Use TagWidget to improve tag input handling
    }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']






