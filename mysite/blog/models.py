import django
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from taggit.managers import TaggableManager
from django.shortcuts import reverse
import datetime
from django.utils import timezone


# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = HTMLField()
    points = models.IntegerField(default=0)
    profile_pic = ResizedImageField(size=[160, 90], quality=100, upload_to="author-pfp", default=None, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.user.username}{timezone.now()}')
        super(Author, self).save(*args, **kwargs)

    def __str__(self):
        return self.fullname
    
    @property
    def num_posts(self):
        return Post.objects.filter(user=self).count()

    def get_url(self):
        return reverse("accounts:profile", kwargs={
            "author_slug": self.slug
        })


class Catagory(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)


    class Meta:
        verbose_name_plural = "Catagories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Catagory, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    @property
    def num_posts(self):
        return Post.objects.filter(catagory=self).count()

    @property
    def last_post(self):
        return Post.objects.filter(catagory=self).latest("date")

class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]

    class Meta:
        verbose_name_plural = 'Replies'


class Comment(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    replies = models.ManyToManyField(Reply, blank=True)

    def __str__(self):
        return self.content[:50]


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = HTMLField(max_length=500)
    catagory = models.ManyToManyField(Catagory)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    upvotes = models.ManyToManyField(User, related_name='post_upvotes')
    downvotes = models.ManyToManyField(User, related_name='post_downvotes')
    tags = TaggableManager()
    comments = models.ManyToManyField(Comment, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.title}{datetime.date.today()}{self.user.user.username}{timezone.now()}')
            print(self.slug)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("blog:blog-post", kwargs={
            "slug": self.slug
        })
    
    def get_score(self):
        upvotes = self.upvotes.all().count()
        downvotes = self.downvotes.all().count()
        return upvotes - downvotes