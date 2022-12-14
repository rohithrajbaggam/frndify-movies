# Generated by Django 3.2.7 on 2022-11-23 19:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0002_saveapitokenmodel_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='userSearchHistoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=500, null=True)),
                ('search_keyword', models.CharField(blank=True, max_length=500, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('lastupdated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_search_history_fkey', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
