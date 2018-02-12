import django.db.models.options as options
from django.db import models

# models.py

class Car(models.Model):
    owner_name = models.CharField(max_length = 500)
    color = models.CharField(max_length = 500)
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (4, "SUV"),
    ])
    created = models.DateTimeField()