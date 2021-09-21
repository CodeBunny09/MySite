from django.contrib import admin
from .models import Project, Me, Hobbies

# Register your models here.
admin.site.register(Project)
admin.site.register(Me)
admin.site.register(Hobbies)