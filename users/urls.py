from django.contrib import admin
from django.urls import path, include
from .views import OAuthLoginView

urlpatterns = [
    path('auth/<str:backend>/', OAuthLoginView.as_view(), name='oauth_login'),
]
