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

#entidade ACHOU do modelo conceitual
class Achado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	
	#referente ao relacionamento com produto
	usuario = models.ForeignKey(User) 
	produto = models.ForeignKey(Produto)
	
	#referente ao relacionamento possivel dono, com User
	possiveis_donos = models.ManyToManyField(User, through="Recuperado")

	def __unicode__(self):
		return self.usuario.username + " achou "+ self.produto.descricao

'''
Para adicionar possiveis_donos a um Achado, faz:
digamos que voce tem um objeto Produto que é produto1 e um User que é user1. Então faz:

achado1 = Recuperado(usuario=user1, achado=produto1)
achado1.save()
---
Pra acessar os usuarios que "recuperaram" um perdido, faz:
Como Perdido é quem tem o campo ManyToManyField...

achado.possiveis_donos.all()

Se quiser saber o contrario, o que os usuarios encontraram, faz:
user.achado_set.all()
'''	
		
#guarda os possiveis donos e o status dos produtos, representa o relacionamento com USER - É A TABELA QUE GUARDA O MANY TO MANY!	
class Recuperado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(User)
	achado = models.ForeignKey(Achado)
	status = models.BooleanField() # Resolvido

	def __unicode__(self):
		return self.usuario.username+" recuperou "+self.achado.produto.descricao+" achado por "+self.achado.usuario.username

#entidade PERDIDO do modelo conceitual
class Perdido(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	
	#referente ao relacionamento com produto
	usuario = models.ForeignKey(User)
	produto = models.ForeignKey(Produto)
	
	#referente ao relacionamento "encontrou"
	usuarios_encontraram = models.ManyToManyField(User, through="Encontrado")
	
	def __unicode__(self):
		return self.usuario.username+" perdeu "+self.produto.descricao

'''
Pra acessar os usuarios que "encontraram" um perdido, faz:
Como Perdido é quem tem o campo ManyToManyField...

perdido.usuarios_encontraram.all()

Se quiser saber o contrario, o que os usuarios encontraram, faz:
user.perdido_set.all()
'''	
		
#representa o relacionamento MxN entre Produto e Perdido
class Encontrado(models.Model):
	data_registro = models.DateField('data registro', auto_now_add=True)
	usuario = models.ForeignKey(User)
	perdido = models.ForeignKey(Perdido)
	status = models.BooleanField() # Resolvido

	def __unicode__(self):
		return self.usuario.username+" encontrou "+self.perdido.produto.descricao+" de "+self.perdido.usuario.username

