from .views import UserDetailView
from django.urls import path

urlpatterns = [
    path("users/", UserDetailView.as_view()),
    path("users/<int:pk>/", UserDetailView.as_view()),
]
