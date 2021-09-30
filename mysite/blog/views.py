from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Author, Catagory, Post
from .utils import update_views
from django.contrib.auth.decorators import login_required
from .forms import PostForm
# Create your views here.

def index(req):
    posts = Post.objects.all()[::-1]
    context = {
        'posts': posts
    }

    return render(req, 'home.html', context=context)

def post(req, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {
        'post': post
    }
    update_views(req, post)
    return render(req, 'post.html', context)

def query(req):
    return render(req, 'post-query.html')

@login_required
def make_post(req):
    context = {}
    form = PostForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            author = Author.objects.get(user=req.user)
            form.save(commit=False)
            form.save_m2m()
            new_post = form
            new_post.user = author
            new_post.save()
            return redirect('blog:blog-index')
    context.update({
        'form': form,
        'title': 'Create A Post'
    })

    return render(req, 'create.html', context)


@login_required
def network_stats(req):
    return render(req, 'network-stats.html')
