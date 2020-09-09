from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Medicion(models.Model):
    cedula = models.CharField(max_length=9)
    nombre = models.CharField(max_length=200)
    edad = models.IntegerField()
    fecha = models.DateTimeField(default = timezone.now)
    peso = models.FloatField()
    imc = models.FloatField()
    pct_grasa_total = models.FloatField()
    pct_agua = models.FloatField()
    musculo_corporal = models.FloatField()
    calificacion = models.FloatField()
    masa_osea = models.FloatField()
    tasa_metabolismo = models.FloatField()
    edad_metabolica = models.FloatField()
    grasa_visceral = models.FloatField()
    masa_magra_bi = models.FloatField()
    masa_magra_bd = models.FloatField()
    masa_magra_pi = models.FloatField()
    masa_magra_pd = models.FloatField()
    masa_magra_tronco = models.FloatField()
    grasa_segmental_bi = models.FloatField()
    grasa_segmental_bd = models.FloatField()
    grasa_segmental_pi = models.FloatField()
    grasa_segmental_pd = models.FloatField()
    grasa_segmental_tronco = models.FloatField()
