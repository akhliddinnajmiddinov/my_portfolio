# Generated by Django 5.1.1 on 2024-09-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blog_imagefield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imageField',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]