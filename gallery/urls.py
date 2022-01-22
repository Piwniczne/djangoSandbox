from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gallery-home'),
    path('category/<slug:slug>', views.categoryPage, name='gallery-image-category'),
    path('category/<slug:slugCategory>/<slug:slugImage>', views.imageDetailPage, name='gallery-image-detail'),
]
