from django.urls import path
from .views import *

urlpatterns = [
  path("get-details",UserDetailAPI.as_view()),
  path("all-user-details",AllUserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]