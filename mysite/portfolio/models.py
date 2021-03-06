from django.db import models
from django.db.models.base import Model

class Project(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='project-thumbnails')
    description = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title

class Me(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    pfp = models.ImageField(upload_to='pfp/')

    def __str__(self) :
        return self.name

    def __repr__(self) :
        return self.name

    class Meta:
        verbose_name_plural = "Me"

class Hobbies(models.Model):
    title = models.CharField(max_length=20)
    icon = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    def __repr__(self) :
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 254)
    subject = models.CharField(max_length=200, default=None, null=True)
    message = models.CharField(max_length=5000)
    date = models.DateField(auto_now_add=True, blank=True)


    def __str__(self):
        return f'{self.name} said {self.message[:50]}'

    def __repr__(self) :
        return f'{self.name} said {self.message[:50]}'