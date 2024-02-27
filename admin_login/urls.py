# admin_login/urls.py
from django.urls import path
from .views import AdminLoginView

urlpatterns = [
    path('api/login/', AdminLoginView.as_view(), name='admin_login'),
]

