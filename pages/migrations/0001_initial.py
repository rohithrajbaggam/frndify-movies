# Generated by Django 3.2.7 on 2022-11-23 11:37

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
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_profile', models.ImageField(default='group.png', upload_to='page_profile')),
                ('page_title', models.CharField(max_length=100, unique=True)),
                ('about', models.TextField(max_length=500)),
                ('field', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('your_role', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True)),
                ('whatsapp', models.CharField(blank=True, max_length=10)),
                ('linkdin_profile_link', models.URLField(blank=True)),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('posted_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, upload_to='page_post_images')),
                ('content', models.TextField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_posts', to=settings.AUTH_USER_MODEL)),
                ('post_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
            ],
            options={
                'ordering': ['-updated', '-created'],
            },
        ),
        migrations.CreateModel(
            name='SavePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='save_Post', to='pages.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
