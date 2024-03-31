# Generated by Django 4.2.5 on 2023-09-05 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0002_remove_user_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('starting_location', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
