# Generated by Django 5.1.1 on 2024-10-05 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_alter_blog_datecreated_alter_blog_imagefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 10, 42, 20, 1873)),
        ),
    ]
