# Generated by Django 3.2.7 on 2022-11-23 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_usersearchhistorymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersearchhistorymodel',
            name='api_key',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
