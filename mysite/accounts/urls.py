from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='account-register'),
    path('delete/', views.delete_profile, name='account-delete'),
    path('login/', views.login_, name='account-login'),
    path('logout/', views.logout, name='account-logout'),
    path('profile-settings/', views.update_profile, name='account-profile'),
    path('profile/<author_slug>', views.profile, name='profile'),
    path('fufollow/<slug>', views.follow_unfollow, name='follow-unfollow'),
    path('network-stats/<slug>', views.net_stats, name='net-stats'),
]