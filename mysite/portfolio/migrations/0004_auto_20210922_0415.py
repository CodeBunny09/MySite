# Generated by Django 3.2.5 on 2021-09-21 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_hobbies_me'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(default=None, max_length=200, null=True)),
                ('message', models.CharField(max_length=5000)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='me',
            options={'verbose_name_plural': 'Me'},
        ),
        migrations.AlterField(
            model_name='hobbies',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]