from django.contrib import admin
from blog.models import Author, Catagory, Post, Comment, Reply
# Register your models here.

admin.site.register(Author)
admin.site.register(Catagory)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reply)