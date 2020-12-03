from django.urls import path,include
from backend.user.views import UserByToken

urlpatterns = [
    path('user/by/token/', UserByToken.as_view()),
]