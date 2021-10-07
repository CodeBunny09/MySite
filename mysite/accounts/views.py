from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lt
from .forms import UpdateForm
from blog.models import Post, Author, AuthorMeta
from django.contrib.auth import get_user


# Create your views here.
def register(req):
    context = {}
    form = UserCreationForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            new_user = form.save()
            authenticate(req, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(req, new_user)
            return redirect("accounts:account-profile")
    context.update({
        "form": form,
        "title": "Signup",
    })
    return render(req, 'register.html', context)

def login_(req):
    context = {}
    form = AuthenticationForm(req, data=req.POST)
    if req.method == "POST":
        if form.is_valid():
            user = authenticate(req, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(req, user)
                return redirect("blog:blog-index")
    context.update({
        'form': form,
        "title": "Login"
    })
    return render(req, 'login.html', context)


@login_required
def update_profile(req):
    context = {}
    user = req.user
    form = UpdateForm(req.POST, req.FILES)
    author = Author.objects.filter(user=user)
    if req.method == "POST":
        if form.is_valid():
            updated_profile = form.save(commit=False)
            updated_profile.user = user
            print("user id: ", user.id)
            author.update_or_create(
                user_id=user.id,
                fullname=updated_profile.fullname,
                bio=updated_profile.bio,
                profile_pic=updated_profile.profile_pic
            )
            return redirect("blog:blog-index")
    context.update({
        "form": form,
        "Title": "Update Profile",
        'user': author
    })
    return render(req, 'profile.html', context)

@login_required
def logout(req):
    lt(req)
    return redirect("blog:blog-index")

@login_required
def profile(req, author_slug):
    context = {}
    user = req.user
    author =  Author.objects.get(slug = author_slug)
    meta = AuthorMeta.objects.get(user = author)
    posts = Post.objects.filter(user=author)[::-1]
    context.update({
        'author': author,
        'posts': posts,
        'meta': meta,
    })
    return render(req, 'profile-pub.html', context)

@login_required
def delete_profile(req):
    user = req.user
    user.delete()

    return redirect("blog:blog-index")

@login_required
def follow_unfollow(req, slug):
    if req.method == "POST":
        # Current User
        user = req.user
        current_author = Author.objects.get(user = user)
        current_author_meta = AuthorMeta.objects.get(user = current_author)
        
        # Viewed User
        id = req.POST.get("author_id")
        author = Author.objects.get(id = id)
        author_meta = AuthorMeta.objects.get(user = author)
        
        # Actions
        if current_author in [i for i in author_meta.followers.all()]:
            print("User is a follower")
            author_meta.followers.remove(current_author)
            current_author_meta.following.remove(author)
        else:
            print("User is not a follower.")
            author_meta.followers.add(current_author)
            current_author_meta.following.add(author)
        return redirect("accounts:profile", slug)

@login_required
def net_stats(req, slug):
    user = req.user
    author = Author.objects.get(user = user)
    author_meta = AuthorMeta.objects.get(user = author)
    print(user)
    print([i for i in author_meta.followers.all()])
    context = {'author_meta' : author_meta}
    return render(req, "network-stats.html", context)
