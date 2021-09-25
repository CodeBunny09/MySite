from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.
def register(req):
    context = {}
    form = UserCreationForm(req.POST or None)
    if req.method == "POST":
        if form.is_valid():
            new_user = form.save()
            authenticate(req, username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(req, new_user)
            return redirect("blog:blog-index")
    context.update({
        "form": form,
        "title": "Signup",
    })
    return render(req, 'register.html', context)