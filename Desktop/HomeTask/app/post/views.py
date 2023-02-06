from django.shortcuts import render
from rest_framework.viewsets import *
from rest_framework.response import Response
from rest_framework import status
from .models import Forum, Comment
from .serializers import ForumSerializer, CommentSerializer
from .permissions import ForumPermission


class ForumViewSet(ModelViewSet):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    permission_classes = [ForumPermission, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [ForumPermission, ]

    def get_queryset(self):
        return super().get_queryset().filter(forum_id=self.kwargs.get('forum_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        forum_id=self.kwargs.get('forum_id'))

