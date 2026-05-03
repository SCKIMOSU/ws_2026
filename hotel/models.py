from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=200)
    reserve_date = models.DateField()
    room_num= models.IntegerField()

    def __str__(self):
        return f"{self.name} /{self.reserve_date}/ {self.room_num}"

class Customer(models.Model):
    name = models.CharField(max_length=200)
    age= models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} / {self.age} / {self.address}"