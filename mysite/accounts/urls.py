from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name='account-register'),
    path('login/', views.login_, name='account-login'),
]