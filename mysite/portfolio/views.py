from django.shortcuts import render
from portfolio.models import Project

# Create your views here.
def index(req):
    projects = Project.objects.all()

    return render(req, 'index.html', {'projects': projects})

def contact(req):
    return render(req, 'contact.html')