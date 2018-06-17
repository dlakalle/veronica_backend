# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    cedula = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    telefono = models.CharField(max_length=200, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    def __unicode__(self):
        return self.cedula + " - " + self.nombre

class Domicilio(models.Model):
    alumno = models.ForeignKey('Alumno', on_delete=models.CASCADE)
    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE)

class Direccion(models.Model):
    direccion = models.CharField(max_length=200, null=True, blank=True)
    comuna = models.CharField(max_length=200, null=True, blank=True)

class Periodo(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    actual = models.BooleanField(default=False)
    def __unicode__(self):
        return self.nombre

class Sede(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Jornada(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Escuela(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=200)
    escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.escuela.__unicode__() + " / " + self.nombre

class PlanEstudio(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre

class CarreraPlan(models.Model):
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE, related_name='sedes')
    jornada = models.ForeignKey(Jornada, on_delete=models.CASCADE, related_name='jornadas')
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name='carreras')
    planestudio = models.ForeignKey(PlanEstudio, on_delete=models.CASCADE, related_name='planes')
    def __unicode__(self):
        return self.sede.__unicode__() + " / " + self.jornada.__unicode__() + " / " + self.carrera.__unicode__() + " / " + self.planestudio.__unicode__()

class Matricula(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name='matriculas')
    planestudio = models.ForeignKey(CarreraPlan, on_delete=models.CASCADE, related_name='matriculas')
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, related_name='matriculas')
    estado = models.ForeignKey('EstadoMatricula', on_delete=models.CASCADE, related_name='matriculas')
    # atributos = JSONField(default=dict)
    def __unicode__(self):
        return self.alumno.__unicode__() + " | " + self.planestudio.__unicode__() + " | " + self.periodo.__unicode__()

class EstadoMatricula(models.Model):
    nombre = models.CharField(max_length=200)
    persiste = models.IntegerField(default=0)

class Alerta(models.Model):
    creador = models.ForeignKey(User, related_name='alertas_creadas')
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='alertas')
    responsable = models.ForeignKey(User, related_name='alertas')
    tipo_alerta = models.ForeignKey('TipoAlerta')
    estado = models.ForeignKey('EstadoAlerta')

class TipoAlerta(models.Model):
    nombre = models.CharField(max_length=128L)
    def __unicode__(self):
        return u'%s' % (self.nombre)

class EstadoAlerta(models.Model):
    nombre = models.CharField(max_length=128L)
    def __unicode__(self):
        return u'%s' % (self.nombre)

class Asignatura(models.Model):
    nombre = models.CharField(max_length=128L)
    def __unicode__(self):
        return u'%s' % (self.nombre)
