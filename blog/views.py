from .models import Post

from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView, DetailView, CreateView


def about(request: HttpRequest):
    context = {
        "title": "About Page",
    }
    return render(request, "blog/html/about.html", context)


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/html/home.html"
    ordering = ["-created_on"]


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
