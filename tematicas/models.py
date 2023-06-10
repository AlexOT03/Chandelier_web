from django.db import models

# Create your models here.
class Theme(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(blank=True)
    images = models.ImageField(upload_to="imagenes")