# Generated by Django 3.2.5 on 2021-10-04 23:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20211004_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='haha',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='haha',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
