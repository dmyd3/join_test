from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Alvo(models.Model):

    nome = models.CharField(
        verbose_name='Nome',
        max_length=200,
    )

    latitude = models.FloatField(
        verbose_name='Latitude',
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )

    longitude = models.FloatField(
        verbose_name='Longitude',
        validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)]
    )

    expiration_date = models.DateField()

    def __str__(self):
        return self.nome +'::'+ str(self.longitude) +','+ str(self.latitude)