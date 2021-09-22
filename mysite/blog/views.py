from django.shortcuts import render, get_object_or_404
from blog.models import Author, Catagory, Post
from .utils import update_views
# Create your views here.

def index(req):
    return render(req, 'home.html')

def post(req, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    update_views(req, post)
    return render(req, 'post.html', context)

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
    return render(req, 'post-query.html')