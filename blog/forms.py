from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class GenerateRandomPosts(forms.Form):
    amount = forms.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(500)
        ]
    )