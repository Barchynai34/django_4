from django.urls import path, include
from users import views
from .views import UserList, UserDetails

urlpatterns = [
    path("users/", include("django.contrib.auth.urls")),
    path("users/register", views.register, name="register"),
    path('users/list/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetails.as_view(), name='user-detail'),
]