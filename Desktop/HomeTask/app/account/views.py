from django.shortcuts import render
from rest_framework import status

from .models import Author
from .serializers import AuthorSerializer
from rest_framework.generics import CreateAPIView, ListAPIView


class RegisterCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

