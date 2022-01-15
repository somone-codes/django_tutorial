"""django_tutorial URL Configuration
"""

from users.views import register
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('blog.urls')),
    path("register/", register, name="register"),
    path("login/", LoginView.as_view(template_name="users/html/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="users/html/logout.html"), name="logout"),
]
