from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class HashtagForProject(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + self.content

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    mini_description = models.CharField(max_length=300, default="")
    dateCreated = models.DateTimeField(default=datetime.now())
    imageField = models.ImageField(upload_to="projects/projects_pics", default="projects/projects_pics/default.png", null = True)
    viewsCount = models.IntegerField(default=0)
    hashtags = models.ManyToManyField(HashtagForProject, blank = True, related_name = "projects")
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(self.dateCreated))
        return super().save(*args, **kwargs)