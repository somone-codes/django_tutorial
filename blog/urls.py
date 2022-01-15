from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostListView.as_view(), name="blog-home"),
    path("about", views.about, name="blog-about"),
]
