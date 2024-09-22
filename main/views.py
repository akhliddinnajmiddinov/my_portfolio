from django.shortcuts import render
from django.http import request
from django.template import Template
# Create your views here.


def HomePageView(request):
    return render(request, "main/index.html")