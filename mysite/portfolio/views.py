from django.shortcuts import render
from portfolio.models import Project, Me, Hobbies, Contact
from portfolio.forms import ContactForm

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
    form = ContactForm(req.POST)
    if req.method == 'POST':
        print(form.data)
        form.save()
    return render(req, 'contact.html', {'form': form})