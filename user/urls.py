from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.homepage, name='homepage'),
    path('homepage/availablecars/', views.availablecars, name='available_cars'),
    path('homepage/availablecars/bookcar/<str:no>/<str:price>/', views.bookcar, name='bookcar'),
    path('homepage/availablecars/book_car/', views.book_car, name='book_car'),
    path('homepage/mybookings/', views.bookinglists, name='bookinglist'),
    path('logout/', views.logout, name='logout'),
  # Add more URL patterns for your app views here
]
