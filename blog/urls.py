from django.urls import path
from . import views
from .views import AddArticleView, HomeView, ArticleView

urlpatterns = [
    # path('', views.home, name='blog-home')
    path('', HomeView.as_view(), name='blog-home'),
    path('article/<int:pk>', ArticleView.as_view(), name='blog-article'),
    path('article/add', AddArticleView.as_view(), name='blog-article-add'),
]