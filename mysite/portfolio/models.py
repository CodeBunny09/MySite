from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='project-thumbnails')
    description = models.CharField(max_length=200)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.title