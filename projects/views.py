from django.shortcuts import render, get_object_or_404
from django.http import request
from .models import Project, HashtagForProject


def ProjectsView(request):
    projects = Project.objects.order_by("-dateCreated")
    context = {
        "hashtags": HashtagForProject.objects.all(),
        "projects": projects
    }
    return render(request, "projects/projects.html", context=context)


def ProjectsWithHashtagView(request, id):
    hashtag = get_object_or_404(HashtagForProject, pk = id)

    projects = hashtag.projects.order_by("-dateCreated")
    context = {
        "queriedHashtag": hashtag,
        "hashtags": HashtagForProject.objects.all(),
        "projects": projects
    }
    return render(request, "projects/projects.html", context=context)


def ProjectView(request, slug):
    project = get_object_or_404(Project, slug=slug)
    project.viewsCount += 1
    project.save()
    context = {
        "project": project
    }
    return render(request, "projects/project.html", context=context)