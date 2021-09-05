from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, 'index.html')

def contact(req):
    return render(req, 'contact.html')