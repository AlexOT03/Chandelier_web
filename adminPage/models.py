from django.db import models

# Create your models here.
class Zones(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="imagenes", null=True)
    
    def __str__(self):
        return self.name

class TipeEvent(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="imagenes", null=True)
    
    def __str__(self):
        return self.name

class Locations(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    discharge_day = models.DateField(auto_now_add=True)
    user_discharge_day = models.DateField(null=True)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="imagenes", null=True)
    
    def __str__(self):
        return self.name

class FastQuote(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=10)
    tipe = models.ForeignKey(TipeEvent, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zones, on_delete=models.CASCADE)
    date = models.DateField()
    message = models.TextField(blank=True)
    
    def __str__(self):
        return self.username