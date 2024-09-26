from django.shortcuts import render, get_object_or_404
from django.http import request
from .models import Blog, Hashtag

# Create your views here.

def BlogsView(request):
    blogs = Blog.objects.order_by("-dateCreated")
    context = {
        "hashtags": Hashtag.objects.all(),
        "blogs": blogs
    }
    return render(request, "blogs/blogs.html", context=context)


def BlogsWithHashtagView(request, id):
    hashtag = get_object_or_404(Hashtag, pk = id)

    blogs = hashtag.posts.order_by("-dateCreated")
    context = {
        "queriedHashtag": hashtag,
        "hashtags": Hashtag.objects.all(),
        "blogs": blogs
    }
    return render(request, "blogs/blogs.html", context=context)