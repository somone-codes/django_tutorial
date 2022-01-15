from .models import Post

from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def about(request: HttpRequest):
    context = {
        "title": "About Page",
    }
    return render(request, "blog/html/about.html", context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/html/home.html"
    ordering = ["-created_on"]


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
