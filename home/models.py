from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(default="Ram",max_length=100)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100)
    address = models.TextField(null=True)
    age=models.IntegerField(default=18)

class Car(models.Model):
    car_name=models.CharField(default="Maruti 800",max_length=100)
    speed=models.IntegerField(default=50)
    def __str__(self) -> str:
        return self.car_name

