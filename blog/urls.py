from django.urls import path, include
from . import views
from .views import AddArticleView, AddCategoryView, CategoryListView, HomeView, ArticleView, UpdatePostView, DeletePostView, CategoryView, PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'articles', PostViewSet)

urlpatterns = [
    # path('', views.home, name='blog-home')
    path('', HomeView.as_view(), name='blog-home'),
    path('article/<int:pk>', ArticleView.as_view(), name='blog-article'),
    path('article/add', AddArticleView.as_view(), name='blog-article-add'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='blog-article-edit'),
    path('article/delete/<int:pk>', DeletePostView.as_view(), name='blog-article-delete'),
    path('category', CategoryListView.as_view(), name='blog-category-list'),
    path('category/add', AddCategoryView.as_view(), name='blog-category-add'),
    path('category/<int:pk>', CategoryView.as_view(), name='blog-category'),
    path('api/', include(router.urls))
]