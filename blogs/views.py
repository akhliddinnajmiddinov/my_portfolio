from django.shortcuts import render, get_object_or_404
from django.http import request
from .models import Blog, HashtagForBlog

# Create your views here.

def BlogsView(request):
    blogs = Blog.objects.order_by("-dateCreated")
    context = {
        "hashtags": HashtagForBlog.objects.all(),
        "blogs": blogs
    }
    return render(request, "blogs/blogs.html", context=context)


def BlogsWithHashtagView(request, id):
    hashtag = get_object_or_404(HashtagForBlog, pk = id)

    blogs = hashtag.posts.order_by("-dateCreated")
    context = {
        "queriedHashtag": hashtag,
        "hashtags": HashtagForBlog.objects.all(),
        "blogs": blogs
    }
    return render(request, "blogs/blogs.html", context=context)


def BlogView(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    blog.viewsCount += 1
    blog.save()
    context = {
        "blog": blog
    }
    return render(request, "blogs/blog.html", context=context)