from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('post/<slug>', views.post, name='blog-post'),
    path('create/', views.make_post, name='post-blog'),
    path('profile/', views.profile, name='blog-private-profile'),
    path('profile-pub/', views.profile_pub, name='blog-public-profile'),
    path('network-stats/', views.network_stats, name='blog-net-stats'),
    path('query/', views.query, name='blog-query'),
]