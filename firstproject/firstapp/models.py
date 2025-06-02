from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name  = models.CharField(max_length=255)
    price = models.IntegerField()

class reservation(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    guests = models.IntegerField()
    comments = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)