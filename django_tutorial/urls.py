"""django_tutorial URL Configuration
"""

from users.views import register
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('blog.urls')),
    path("register/", register, name="register"),
]
