from django.shortcuts import render
from django.http import HttpRequest

posts = [
    {
        "author": "Someone",
        "title": "Obligatory First post",
        "created_on": "14-01-2022",
        "content": "Hello there, this is my first post ever!"
    },
    {
        "author": "Someone 2",
        "title": "Following up on the first post",
        "created_on": "14-01-2022",
        "content": "Hit me up, lets chat."
    }
]


def home(request: HttpRequest):
    context = {
        "title": "Welcome to blog's",
        "posts": posts
    }
    return render(request, "blog/html/home.html", context)


def about(request: HttpRequest):
    context = {
        "title": "About Page",
    }
    return render(request, "blog/html/about.html", context)
