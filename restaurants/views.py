from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from .serializers import RestaurantSerializer, ReviewSerializer

from .models import Restaurant, Review
# Create your views here.
