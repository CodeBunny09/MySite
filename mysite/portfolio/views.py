from django.shortcuts import render
from portfolio.models import Project, Me, Hobbies

# Create your views here.
def index(req):
    projects = Project.objects.all()
    my_details = Me.objects.all()
    hobbies = Hobbies.objects.all()
    context = {
        'projects' : projects,
        'me': my_details,
        'hobbies': hobbies
    }
    return render(req, 'index.html', context)

def contact(req):
    return render(req, 'contact.html')