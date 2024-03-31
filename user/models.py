from django.db import models

# Define the Car model
class Car(models.Model):
    car_number = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='static/car_images/')
    rent_price = models.DecimalField(max_digits=10, decimal_places=2)
    seater = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=10)

    def __str__(self):
        return self.car_number