from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer

class userCreating(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserRUD(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
# Create your views here.
