from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Author, Catagory, Post, Comment, Reply
from .utils import update_views
from django.contrib.auth.decorators import login_required
from .forms import PostForm
# Create your views here.

def index(req):
    posts = Post.objects.all()[::-1]
    num_posts = Post.objects.all().count()
    num_users = Author.objects.all().count()
    
    context = {
        'posts': posts,
        'num_posts' : num_posts,
        'num_users' : num_users,
    }

    return render(req, 'home.html', context=context)

def post(req, slug):
    post = get_object_or_404(Post, slug=slug)

    if "comment-form" in req.POST:
        author = Author.objects.get(user=req.user)
        comment = req.POST.get("comment")
        new_comment, created = Comment.objects.get_or_create(user = author, content=comment)
        post.comments.add(new_comment.id)

    if "reply-form" in req.POST:
        author = Author.objects.get(user=req.user)
        reply = req.POST.get("reply")
        comment_id = req.POST.get("comment-id")
        comment_obj = Comment.objects.get(id=comment_id)
        new_reply, created = Reply.objects.get_or_create(user = author, content=reply)
        comment_obj.replies.add(new_reply)
    
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
            new_post = form.save(commit=False)
            new_post.user = author
            new_post.save()
            form.save_m2m()
            return redirect('blog:blog-index')
    context.update({
        'form': form,
        'title': 'Create A Post'
    })

    return render(req, 'create.html', context)


@login_required
def network_stats(req):
    return render(req, 'network-stats.html')
