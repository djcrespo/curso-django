from django.db import models
from apps.empresas.models import empresaRepresentante

# Create your models here.
class computadora(models.Model):
  id = models.BigAutoField(primary_key=True, editable=False)
  modelo = models.CharField(max_length=50, null=True)
  caracteristicas = models.JSONField()

  def __str__(self):
    return str(self.id)

class telefono(models.Model):
  id = models.BigAutoField(primary_key=True, editable=False)
  modelo = models.CharField(max_length=50, null=True)
  caracteristicas = models.JSONField()

  def __str__(self):
    return str(self.id)
  
class computadoraEmpresa(models.Model):
  computadora = models.ManyToManyField(computadora)
  empresa = models.ForeignKey(empresaRepresentante, on_delete=models.CASCADE)