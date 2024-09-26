from django.db import models


# Create your models here.
class Hashtag(models.Model):
    content = models.CharField(max_length=100)


    def __str__(self):
        return str(self.id) + self.content

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=10000)
    dateCreated = models.DateTimeField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag, blank = True, related_name = "posts")
    

    def __str__(self):
        return self.title