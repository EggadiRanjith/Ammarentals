from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # You should store hashed passwords, not plain text
    
    is_admin = models.IntegerField(
        default=0,
        choices=[
            (0, 'No'),  # 0 represents 'No'
            (1, 'Yes'),  # 1 represents 'Yes'
        ],)
    def __str__(self):
        return self.username
