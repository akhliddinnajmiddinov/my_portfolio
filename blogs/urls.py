from django.urls import path
from . import views


app_name = "blogs"

urlpatterns = [
    path("", views.BlogsView, name = "blogs"),
    path("hashtag/<int:id>", views.BlogsWithHashtagView, name = "blogsWithHashtag"),
]