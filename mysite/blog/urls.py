from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('post/', views.post, name='blog-post'),
    path('login/', views.login, name='blog-login'),
    path('signup/', views.signup, name='blog-signup'),
    path('profile/', views.profile, name='blog-private-profile'),
    path('profile-pub/', views.profile_pub, name='blog-public-profile'),
    path('network-stats/', views.network_stats, name='blog-net-stats'),
    path('query/', views.query, name='blog-query'),
]