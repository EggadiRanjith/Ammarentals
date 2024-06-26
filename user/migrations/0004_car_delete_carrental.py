# Generated by Django 4.2.4 on 2023-09-08 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_carrental_delete_carrentals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=15, unique=True)),
                ('image', models.ImageField(upload_to='car_images/')),
                ('rent_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('seater', models.PositiveIntegerField()),
                ('fuel_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='CarRental',
        ),
    ]
