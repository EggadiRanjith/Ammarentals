from django.db import models
from user.models import Car  # Import the Car model if not already done

class Booking(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    car_number = models.CharField(max_length=15)  # Car number field
    pickup_date = models.DateField()
    return_date = models.DateField()
    total_number_of_days = models.PositiveIntegerField()
    totalprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
