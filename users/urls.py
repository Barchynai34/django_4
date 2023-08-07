from django.urls import path, include
from users import views

urlpatterns = [
    path("users/", include("django.contrib.auth.urls")),
    path("users/register", views.register, name="register"),
]