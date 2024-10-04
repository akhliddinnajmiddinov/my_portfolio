from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify


# Create your models here.
class Hashtag(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + self.content

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    dateCreated = models.DateTimeField(default=datetime.now())
    imageField = models.ImageField(upload_to="blogs/blogs_pics", default=None)
    viewsCount = models.IntegerField(default=0)
    hashtags = models.ManyToManyField(Hashtag, blank = True, related_name = "posts")
    slug = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(self.dateCreated))
        return super().save(*args, **kwargs)