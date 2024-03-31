from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='amma'),
    path('register',views.register,name='register'),
    path('loginvalidation',views.login,name='loginvalidation')
    
  # Add more URL patterns for your app views here
]
