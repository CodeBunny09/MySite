from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portfolio-index'),
    path('contact', views.contact, name='portfolio-contact-me')
]