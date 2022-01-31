from traceback import format_stack
from django import forms
from .models import Post, Category

# choices = [('cat1', 'cat1'), ('cat2', 'cat2')]
# choices = Category.objects.all().value_list('name', 'name')
# query to list
# choice_list = []
# for item in choices:
#     choice_list.append(item)
#

#create form field for model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body','category') # ,'thumbnail'

        widgets = {
            # we create input text as default but adds some css
            # forms may be get from the bootstrap https://getbootstrap.com/docs/5.1/forms/overview/
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user_id', 'type': 'hidden'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # choices must be first
            # 'category': forms.Select(choices = choices, attrs={'class': 'form-control'}),
            # 'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body','category')

        widgets = {
            # we create input text as default but adds some css
            # forms may be get from the bootstrap https://getbootstrap.com/docs/5.1/forms/overview/
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # 'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', 'description') # ,'thumbnail'

        widgets = {
            # we create input text as default but adds some css
            # forms may be get from the bootstrap https://getbootstrap.com/docs/5.1/forms/overview/
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }