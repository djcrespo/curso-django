from django.db import models

# Create your models here.
class empresa(models.Model):
  id = models.BigAutoField(primary_key=True, editable=False)
  nombre = models.CharField(max_length=50, null=False)
  direccion = models.CharField(max_length=255, null=False)
  telefono_empresa = models.CharField(max_length=15, blank=True, null=True)

  def __str__(self):
    return str(self.id)
  
class representante(models.Model):
  id = models.BigAutoField(primary_key=True, editable=False)
  nombre = models.CharField(max_length=50, null=False)
  apellido_paterno = models.CharField(max_length=50, null=False)
  Apellido_materno = models.CharField(max_length=50, null=False)
  telefono = models.CharField(max_length=15, blank=True, null=True)

  def __str__(self):
    return f"{self.nombre} {self.apellido_paterno}"
  
class empresaRepresentante(models.Model):
  empresa = models.OneToOneField(empresa, verbose_name="Empresa que representa la persona", on_delete=models.CASCADE)
  representante = models.ManyToManyField(representante)
  fecha_actualizacion = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.empresa.id)