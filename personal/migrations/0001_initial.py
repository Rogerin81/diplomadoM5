# Generated by Django 5.1.4 on 2024-12-09 02:07

import django.db.models.deletion
import personal.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('ci', models.CharField(max_length=10, unique=True, validators=[personal.models.validar_ci])),
                ('salario', models.DecimalField(decimal_places=2, max_digits=10, validators=[personal.models.validar_salario])),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='personal.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField(blank=True, null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Vacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.empleado')),
            ],
        ),
    ]
