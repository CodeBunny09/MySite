from django.contrib import admin
from .models import Project, Me, Hobbies, Contact
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
admin.site.register(Project)
admin.site.register(Me)
admin.site.register(Hobbies)

class ContactResource(resources.ModelResource):
    class Meta:
        model = Contact

class ContactAdmin(ImportExportActionModelAdmin):
    resource_class = ContactResource
    ordering = ('date',)
    list_display = ('id', 'name', 'email', 'subject', 'message', 'date')


admin.site.register(Contact, ContactAdmin)