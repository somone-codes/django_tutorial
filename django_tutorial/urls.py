"""django_tutorial URL Configuration
"""

from users.views import register, profile, UserProfileView
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
    path("register/", register, name="register"),
    path("profile/<pk>", UserProfileView.as_view(), name="user-profile-detail"),
    path("profile/", profile, name="profile"),
    path("login/", LoginView.as_view(template_name="users/html/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="users/html/logout.html"), name="logout"),
]

if settings.DEBUG:
    # this is for local development serving only, for prod look into django doc
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
