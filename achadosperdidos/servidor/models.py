# -*- coding: utf-8 -*-
#comentario acima para poder aceitar acentos e caracteres especiais

from django.db import models
from django.db.models.fields import *

# Create your models here.

class Usuario (models.Model):
	login = models.CharField(max_length=7, primary_key = True)
	senha = models.CharField(max_length=15)
	nome = models.CharField(max_length=100)
	permissao = models.CharField(max_length=100)
	
	def __unicode__(self):
		return "Usuario: " + self.login + " || " + self.nome + " || " + self.permissao

class Produto (models.Model):
	status = models.BooleanField() # Resolvido
	descricao = models.TextField(blank=False)
	tipo = models.CharField(max_length=100)
	
	def __unicode__(self):
		return "Produto: " + self.tipo + " || " + self.descricao

class Achado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(Usuario)
	produto = models.ForeignKey(Produto)

class Recuperado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(Usuario)
	produto = models.ForeignKey(Achado)
	
class Perdido(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(Usuario)
	produto = models.ForeignKey(Produto)

class Encontrado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(Usuario)
	produto = models.ForeignKey(Perdido)
