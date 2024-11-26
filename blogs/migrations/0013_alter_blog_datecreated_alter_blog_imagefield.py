# Generated by Django 5.1.1 on 2024-10-05 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_alter_blog_datecreated_alter_blog_imagefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='dateCreated',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 5, 10, 39, 30, 614229)),
        ),
        migrations.AlterField(
            model_name='blog',
            name='imageField',
            field=models.ImageField(blank=True, default='blogs/blogs_pics/default.png', null=True, upload_to='blogs/blogs_pics'),
        ),
    ]
