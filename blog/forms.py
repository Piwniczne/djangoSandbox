from traceback import format_stack
from django import forms
from .models import Post

#create form field for model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body','category','thumbnail')

        widgets = {
            # we create input text as default but adds some css
            # forms may be get from the bootstrap https://getbootstrap.com/docs/5.1/forms/overview/
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }