from django import template
from django.shortcuts import render

#List- will query dataset for us look for records 
#and bring them back to list it in page
#detailed- the same but one record.
#Generic handles queries etc for us.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import PostForm, EditForm, CategoryForm
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializer import PostSerializer
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
    ordering = ['-created']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        # or super(ListView, self).get_context_data(**kwargs) ?
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        ModifyContextBlogBase(context)
        return context

class ArticleView(DetailView):
    model = Post
    template_name = 'blog/article.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        ModifyContextBlogBase(context)
        return context
  

class AddArticleView(CreateView):
    model = Post
    form_class = PostForm #use our defined class form
    template_name = 'blog/add_article.html'
    # fields = '__all__'
    # fields = ('title', 'body')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        ModifyContextBlogBase(context)
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm # use the same form as for creation
    template_name = 'blog/update_article.html'
    # fields = ['title', 'body', 'category']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_article.html'
    success_url = reverse_lazy('blog-home')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm #use our defined class form
    template_name = 'blog/add_category.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        ModifyContextBlogBase(context)
        return context


class CategoryView(DetailView):
    model = Category
    template_name = 'blog/category.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        ModifyContextBlogBase(context)
        return context  

class CategoryListView(ListView):
    model = Category #use this model. accesed by object_list in template
    template_name = 'blog/category_list.html'
    ordering = ['-pk']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        # or super(ListView, self).get_context_data(**kwargs) ?
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        ModifyContextBlogBase(context)
        return context

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer