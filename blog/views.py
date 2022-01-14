from .models import Post

from django.shortcuts import render
from django.http import HttpRequest


def home(request: HttpRequest):
    context = {
        "title": "Welcome to blog's",
        "posts": Post.objects.all()
    }
    return render(request, "blog/html/home.html", context)


def about(request: HttpRequest):
    context = {
        "title": "About Page",
    }
    return render(request, "blog/html/about.html", context)
