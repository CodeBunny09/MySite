from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('post/<slug>', views.post, name='blog-post'),
    path('create/', views.make_post, name='post-blog'),
    path('network-stats/', views.network_stats, name='blog-net-stats'),
    path('query/', views.query, name='blog-query'),
    path('upvote/<slug>', views.upvote, name='blog-upvote'),
    path('downvote/<slug>', views.downvote, name='blog-downvote'),
    path('haha-comment/<slug>', views.haha_comment, name='comment-haha'),
    path('haha-reply/<slug>', views.haha_reply, name='reply-haha'),
    path('delete-post/<slug>', views.del_post, name='delete-post'),
]