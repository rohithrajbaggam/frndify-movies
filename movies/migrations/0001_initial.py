# Generated by Django 3.2.7 on 2022-11-23 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveAPITokenModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_key', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('lastupdated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='userMovieSuggestionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('lastupdated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_movie_suggestions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
