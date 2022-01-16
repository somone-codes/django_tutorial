from .models import Post

from django.shortcuts import render, get_list_or_404
from django.http import HttpRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

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
    paginate_by = 5


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/html/user_posts.html"
    ordering = ["-created_on"]
    paginate_by = 5

    def get_queryset(self):
        print("000000000000000000000000000000000000000000000000000000")
        user = get_list_or_404(User, username=self.kwargs.get("username"))
        print(user)
        return Post.objects.filter(author=user[0]).order_by("-created_on")


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.get_object().author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        return self.get_object().author == self.request.user