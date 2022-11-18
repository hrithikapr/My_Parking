from django.db import models

# Create your models here.

class Parking(models.Model):

    state = models.CharField(max_length=4)
    vehicle_no = models.CharField(max_length=6, unique=True)
    vehicle_type = models.CharField(max_length=5)
    park_time = models.TimeField()
    park_date = models.DateField()
    park_price = models.IntegerField(default=20)

    def __str__(self):
        return self.vehicle_no
