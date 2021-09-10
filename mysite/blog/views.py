from django.shortcuts import render
# Create your views here.

def index(req):
    return render(req, 'home.html')

def post(req):
    return render(req, 'post.html')

def login(req):
    return render(req, 'login.html')

def signup(req):
    return render(req, 'signup.html')