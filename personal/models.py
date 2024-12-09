from django.db import models
from django.core.exceptions import ValidationError

# Validaciones personalizadas
def validar_ci(ci):
    if not ci.isdigit() or len(ci) < 7 or len(ci) > 10:
        raise ValidationError("El CI debe contener entre 7 y 10 dígitos.")

def validar_salario(salario):
    if salario < 2160:  # Salario mínimo en Bolivia (Bs.)
        raise ValidationError("El salario no puede ser inferior al mínimo nacional.")

#Generacion de tablas para los modelos
class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ci = models.CharField(max_length=10, unique=True, validators=[validar_ci])
    salario = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_salario])
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='empleados')

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.ci})"

class Asistencia(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(blank=True, null=True)

class Vacaciones(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def clean(self):
        if self.fecha_inicio > self.fecha_fin:
            raise ValidationError("La fecha de inicio no puede ser mayor a la fecha de fin.")
