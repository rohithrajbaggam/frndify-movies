# Generated by Django 3.2.7 on 2022-11-23 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221123_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.TextField(blank=True, null=True),
        ),
    ]
