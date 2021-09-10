from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('post/', views.post, name='blog-post'),
    path('login/', views.login, name='blog-login'),
    path('signup/', views.signup, name='blog-signup'),
]