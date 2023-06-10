from django.db import models
from ubicaciones.models import Location
from servicios.models import Service

# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    ubication_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, on_delete=models.CASCADE)
    estimated_price = models.IntegerField(blank=True)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    size = models.IntegerField(default=3)
    date_event = models.DateField(blank=True)
    
class Event(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    quote_id = models.ForeignKey(Quote, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    final_date = models.DateField(blank=True)