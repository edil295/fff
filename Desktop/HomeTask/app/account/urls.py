from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterCreateAPIView


urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view()),
    path('token/', obtain_auth_token),
    path('api/auth/', include('rest_framework.urls')),
]