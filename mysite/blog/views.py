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

def profile(req):
    return render(req, 'profile.html')

def profile_pub(req):
    return render(req, 'profile-pub.html')

def network_stats(req):
    return render(req, 'network-stats.html')


def query(req):
    return render(req, 'query.html')