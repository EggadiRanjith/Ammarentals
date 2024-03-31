from datetime import datetime
from django.shortcuts import render ,redirect
from django.core.exceptions import ValidationError
from .models import *
from ammarentaladmin.models import *

# Create your views here.
def homepage(request):
  return render(request,'homepage.html')

def availablecars(request):
    car =Car.objects.all()
    context = {'car': car}
    return render(request, 'available_cars.html', context)

def bookcar(request, no, price):
    context = {
        'no': no,
        'price': price,
    }
    return render(request, 'bookingcar.html', context)


def book_car(request):
    if request.method == 'POST':
        car_number = request.POST['car_number']
        pickup_date = request.POST['pickup_date']
        return_date = request.POST['return_date']
        total_number_of_days = request.POST['total_number_of_days']
        price = request.POST['price']
        total_price = request.POST['total_price']
        username = request.session.get('user_name')  # Use parentheses ()
        contact = request.session.get('user_mobile')  # Use parentheses ()
        # Create a new Booking instance and save it
        booking = Booking(
            name=username,
            mobile_number=contact,
            car_number=car_number,
            pickup_date=pickup_date,
            return_date=return_date,
            total_number_of_days=total_number_of_days,
            totalprice=total_price
        )
        booking.save()
        return redirect('homepage')  # Redirect to car list view

    return render(request, 'available_cars.html')
  
def bookinglists(request):
    contact = request.session.get('user_mobile') 
    # Retrieve Booking objects from the database
    bookings = Booking.objects.filter(mobile_number=contact)
    # Pass the bookings queryset to the template
    return render(request, 'mybookings.html', {'bookings': bookings})
  
def logout(request):
    # Delete the user's session
    request.session.flush()
    # Redirect to a specific URL (e.g., the home page)
    return redirect('amma')