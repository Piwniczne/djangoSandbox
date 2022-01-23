from django import template
from django.shortcuts import render

#List- will query dataset for us look for records 
#and bring them back to list it in page
#detailed- the same but one record.
#Generic handles queries etc for us.
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

# view as a function
def home(request):
    posts = Post.objects.all()
    context = {}
    context['posts'] = posts
    return render(request, 'blog/home.html', context)

def ModifyContextBlogBase(context):
    context['nbar'] = "blog"
    context['categories'] = Category.objects.all()

#view as a clase
class HomeView(ListView):
    model = Post #use this model. accesed by object_list in template
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        ModifyContextBlogBase(context)
        return context

class ArticleView(DetailView):
    model = Post
    template_name = 'blog/article.html'