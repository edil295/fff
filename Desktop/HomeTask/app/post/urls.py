from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

forum = DefaultRouter()
forum.register('', ForumViewSet)
comment = DefaultRouter()
comment.register('comment', CommentViewSet)


urlpatterns = [
    path('forum/', include(forum.urls)),
    path('forum/<int:forum_id>/', include(comment.urls)),
]
