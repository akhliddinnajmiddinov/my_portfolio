from django.shortcuts import render
from django.http import request

# Create your views here.

def BlogsView(request):
    return render(request, "blogs/blogs.html")