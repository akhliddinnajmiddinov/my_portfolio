from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
    path("", views.ProjectsView, name = "projects"),
    path("<str:slug>", views.ProjectView, name = "project"),
    path("hashtag/<int:id>", views.ProjectsWithHashtagView, name = "projectsWithHashtag"),
]