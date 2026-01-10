from django.urls import path
from .views import user_create


urlpatterns = [path("users/", user_create, name="create_user")]
