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
	TIPOS_CHOICES = ( 
		('pendrive','Pendrive'),
		#('caneta','Caneta'),
		('fonedeouvido','Fone de Ouvido'),
		('carregadorcelular','Carregador de Celular'),
		('carregadornotebook','Carregador de Notebook'),
		#('cabo','Cabo'),
		#('bolsa','Bolsa'),
		('guardachuva', 'Guarda Chuva/Sombrinha'),
		#('cracha', 'Crachá'),
		('outros', 'Outros'),
		#('livrorevista', 'Livro/Revista'),
		#('estojo', 'Estojo'),
	)
	id = models.TextField(primary_key = True)
	status = models.BooleanField() #tem que mudar pra booleano, nao ajeitamos porque o site tá ruim
	descricao = models.TextField(blank=False)
	tipo = models.CharField(max_length=100, choices=TIPOS_CHOICES)
	
	def __unicode__(self):
		return "Produto: " + self.tipo + " || " + self.descricao

class Achou (models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	login_usuario = models.ForeignKey(Usuario)
	id_produto = models.ForeignKey(Produto)

class PossivelDono(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	login_usuario = models.ForeignKey(Usuario)
	id_produto = models.ForeignKey(Achou)
	
class Perdeu (models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	login_usuario = models.ForeignKey(Usuario)
	id_produto = models.ForeignKey(Produto)

class Encontrou (models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	login_usuario = models.ForeignKey(Usuario)
	id_produto = models.ForeignKey(Perdeu)