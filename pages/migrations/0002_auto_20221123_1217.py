# Generated by Django 3.2.7 on 2022-11-23 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_profile',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.TextField(blank=True, null=True),
        ),
    ]
