from django.shortcuts import render,redirect
from user.models import *
from .models import *

# Create your views here.
def ammarentaladmin(request):
  return render(request,'ammarentaladmin/homepage.html')

def admin_availablecars(request):
    car =Car.objects.all()
    context = {'car': car}
    return render(request, 'ammarentaladmin/available_cars.html', context)

def uploadcar(request):
    return render(request,'ammarentaladmin/upload_car.html')

def insert_car(request):
    if request.method == 'POST':
        car_number = request.POST['car_number']
        image = request.FILES['image']
        rent_price = request.POST['rent_price']
        seater = request.POST['seater']
        fuel_type = request.POST['fuel_type']

        # Create a new Car instance and save it
        car = Car(car_number=car_number, image=image, rent_price=rent_price, seater=seater, fuel_type=fuel_type)
        car.save()
        return redirect('admin_available_cars')  # Redirect to a view displaying the list of cars

    return render(request, 'ammarentaladmin/upload_car.html')

def bookings(request):
    # Retrieve Booking objects from the database
    bookings = Booking.objects.all()
    # Pass the bookings queryset to the template
    return render(request, 'ammarentaladmin/bookings.html', {'bookings': bookings})

def logout(request):
    # Delete the user's session
    request.session.flush()
    # Redirect to a specific URL (e.g., the home page)
    return redirect('amma')