from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lt
from .forms import UpdateForm


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
    if req.method == "POST":
        if form.is_valid():
            updated_profile = form.save(commit=False)
            updated_profile.user = user
            updated_profile.save()
            return redirect("blog:blog-index")
    context.update({
        "form": form,
        "Title": "Update Profile"
    })
    return render(req, 'profile.html', context)

@login_required
def logout(req):
    lt(req)
    return redirect("blog:blog-index")