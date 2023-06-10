from django.db import models
from estados.models import State
from tematicas.models import Theme

# Create your models here.
class Hours(models.Model):
    start_hour = models.TimeField(blank=True)
    day = models.DateField(blank=True)

class Location(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    location_length = models.CharField(max_length=200, blank=True, default=0)
    location_width = models.CharField(max_length=200, blank=True, default=0)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE)
    hours_id = models.ForeignKey(Hours, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    created_date= models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="imagenes")