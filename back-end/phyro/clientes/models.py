from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
	usuario = models.ForeignKey(User)
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	preferencias = models.ManyToManyField("Preferencia")

class Proyecto(models.Model):
	titulo = models.CharField(max_length=50)
	requerimientos = models.ManyToManyField("Requerimiento")
	descripcion = models.TextField()
	inicioDisponible = models.DateField()
	finalP = models.DateField()
	presupuesto = models.CharField(max_length=50)
    def __unicode__(self):
        self.titulo

class Etapa(models.Model):
	proyecto = models.ForeignKey("Proyecto")
	titulo = models.CharField(max_length=245)
	descripcion = models.TextField()
	nivel = models.CharField(max_length=50)
    def __unicode__(self):
        return "%s - %s %s"%(self.proyecto, self.titulo,
        					self.nivel)

class Tarea(models.Model):
	etapa = models.ForeignKey("Etapa")
	realizada = models.BooleanField()
	nivel = models.CharField(max_length=50)
	prioridad = models.CharField(max_length=50)
	descripcion = models.TextField()
	fechaTermino = models.DateField()
	resultados = models.TextField()

    def __unicode__(self):
        return "Tareas de %s"%self.etapa.proyecto
    

class Preferencia(modesl.Model):
	preferencia = models.CharField(max_length=50)
	def __unicode__(self):
		return self.preferencia

class Requerimiento(models.Model):
	requerimiento = models.CharField(max_length=50)