from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Producto(models.Model):
    codigo = models.CharField(max_length=255, primary_key=True)
    nombre = models.CharField(max_length=255)
    precio = models.IntegerField()
    img = models.ImageField(upload_to='Fotos/')    



def __str__(self):
    return self.nombre



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
