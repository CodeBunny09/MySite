from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lt
from .forms import UpdateForm
from blog.models import Post, Author
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
            print(dir(author))
            author.update(fullname=updated_profile.fullname)
            author.update(bio=updated_profile.bio)
            author.update(profile_pic=updated_profile.profile_pic)
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
def profile(req):
    context = {}
    user = req.user
    author =  Author.objects.get(user=user)
    posts = Post.objects.filter(user=author)[::-1]
    context.update({
        'author': author,
        'posts': posts,
    })
    return render(req, 'profile-pub.html', context)

@login_required
def delete_profile(req):
    # User = get_user_model()
    user = req.user
    user.delete()
    # user = User.objects.get(id=req.user.id)
    # author = Author.objects.get(user=user)
    # author.delete()
    # user.delete()
    return redirect("blog:blog-index")