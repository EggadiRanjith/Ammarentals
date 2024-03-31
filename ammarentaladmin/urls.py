from django.urls import path
from . import views

urlpatterns = [
    path('ammarentaladmin', views.ammarentaladmin, name='ammarentaladmin'),
    path('ammarentaladmin/availablecars/', views.admin_availablecars, name='admin_available_cars'),
    path('ammarentaladmin/uploadcar/', views.uploadcar, name='upload_car'),
    path('ammarentaladmin/uploadcar/insertcar/', views.insert_car, name='insertcar'),
    path('ammarentaladmin/bookings/', views.bookings, name='bookings'),
    path('logout/', views.logout, name='logout'),
  # Add more URL patterns for your app views here
]
