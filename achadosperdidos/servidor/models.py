# -*- coding: utf-8 -*-
#comentario acima para poder aceitar acentos e caracteres especiais

from django.db import models
from django.db.models.fields import *
from django.contrib.auth.models import User

# Create your models here.

class PerfilUsuario (models.Model):
	usuario = models.OneToOneField(User)
	chaveAtivacao = models.CharField(max_length=40)
	dataExpiracao = models.DateTimeField()
	
	def __unicode__(self):
		return "Usuario: " + self.usuario + " || " + self.chaveAtivacao + " || " + self.dataExpiracao

class Produto (models.Model):
	descricao = models.TextField(blank=False)
	tipo = models.CharField(max_length=100)
	
	def __unicode__(self):
		return "Produto: " + self.tipo + " || " + self.descricao

class Achado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(User)
	produto = models.ForeignKey(Produto)

	def __unicode__(self):
		return self.usuario.username + " achou "+ self.produto.descricao

class Recuperado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(User)
	achado = models.ForeignKey(Achado)
	status = models.BooleanField() # Resolvido

	def __unicode__(self):
		return self.usuario.username+" recuperou "+self.achado.produto.descricao+" achado por "+self.achado.usuario.username
	
class Perdido(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(User)
	produto = models.ForeignKey(Produto)

	def __unicode__(self):
		return self.usuario.username+" perdeu "+self.produto.descricao

class Encontrado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(User)
	perdido = models.ForeignKey(Perdido)
	status = models.BooleanField() # Resolvido

	def __unicode__(self):
		return self.usuario.username+" encontrou "+self.perdido.produto.descricao+" de "+self.perdido.usuario.username
