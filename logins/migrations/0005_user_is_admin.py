# Generated by Django 4.2.4 on 2023-09-08 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logins', '0004_delete_travelinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
    ]
