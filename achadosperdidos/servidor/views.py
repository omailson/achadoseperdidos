# -*- coding: utf-8 -*-

from servidor.models import *
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext
from django.db import IntegrityError

import datetime, random, sha

def paginaLogin(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

#uc-01 fazer login
def fazerLogin(request):
	t = loader.get_template('index.html')
	dados = request.POST
	usuario = authenticate(username = dados['login'], password = dados['senha'])
	if usuario is not None:
		if usuario.is_active:
			login(request, usuario)
			mensagem = 'Login efetuado com sucesso'
			c = RequestContext (request, {
				'mensagem': mensagem
			})
			return HttpResponse(t.render(c))
		else:
			return HttpResponse('Sua conta foi desativada') #Depois criar uma página html para exibir melhor essa mensagem
	else:
		return HttpResponse('Dados incorretos') #Depois criar uma página html para exibir melhor essa mensagem
	
	
#uc-02 logout
def fazerLogout(request):
	logout_then_login('/login/')
	#return HttpResponse("Bye bye")

#temporário, só pra testar a tela	
def telaCadastrarUsuario(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('cadastrarUsuario.html', c)
	
#uc-03 
def cadastrarUsuario(request):
	dados = request.POST
	senha = dados['senha']
	senhaConfirmacao = dados['senhaconfirmacao']
	if senha == senhaConfirmacao: #Verifica se os campos senha e confirmação de senha estão preenchidos iguais
		login = dados['login']
		usuario = User.objects.get(username = login)
		print 'oi'
		if usuario is None: #caso o usuário não exista
			#Criando novo usuário inativo
			newUser = User.objects.create_user(login, login + '@cin.ufpe.br', senha)
			newUser.is_active = false
			newUser.save()
			
			#Construindo a chave de ativação para a conta
			salt = sha.new(str(random.random())).hexdigest()[:5]
			chaveAtivacao = sha.new(salt+new_user.username).hexdigest()
			dataExpiracao = datetime.datetime.today() + datetime.timedelta(2)
			
			c = RequestContext (request, {})
		elif usuario.is_active: #caso já exista um usuário com esse login e sua conta esteja ativa
			c = 'Já existe um usuário com esse login'
		else: #caso já exista um usuário com esse login mas sua conta não esteja ativa
			print 'opa' #mandar e-mail
	else:
		c = 'Você escreveu duas senhas diferentes'
	return HttpResponse(c)

#uc-04
def cadastrarProdutoEncontrado(request):
	return HttpResponse("TEM QUE FAZER!!!")

#uc-05 -- Vanessa_E_Mariana
def cadastrarProduto(request):
	try:
		cadastro = request.POST
		tipoCadastro = cadastro['tipo']
		descricaoCadastro = cadastro["descricao"]
		
		produto = Produto(tipo=tipoCadastro, descricao=descricaoCadastro)
		produto.save()

		# XXX: Pegar usuario 
		u = User.objects.all()[0]

		perdido = Perdido(usuario=u, produto=produto)
		perdido.save()

		resposta = "Cadastro efetuado com sucesso."
	except Exception as e:
		print e
		resposta = "Cadastro inválido. Digite os dados corretamente."

	return HttpResponse(resposta)

def form_cadastrarProduto(request):
	t = loader.get_template('form_cadastrarProdutoPerdido.html')
	c = RequestContext (request)
	c.update(csrf(request))
	return HttpResponse(t.render(c))	

#uc-06 -- Vanessa_E_Mariana
def listarProdutosEncontrados(request):
	produtos = Produto.objects.all()
	resposta = []

	for p in produtos:
		if (p.status == True):
			resposta.append(p)

	return HttpResponse(resposta)

#uc07 -- Vanessa_E_Mariana
def listarProdutosPerdidos(request):
	perdidos = Perdido.objects.all()
	produtos = [x.produto for x in perdidos if not x.produto.status]

	t = loader.get_template('listar_produtos.html')
	c = RequestContext (request, {'produtos': produtos})
	return HttpResponse(t.render(c))	

def listarProdutosAchados(request):
	achados = Achado.objects.all()
	produtos = [x.produto for x in achados if not x.produto.status]

	t = loader.get_template('listar_produtos.html')
	c = RequestContext (request, {'produtos': produtos})
	return HttpResponse(t.render(c))

#uc08 
""" Alguem achou algum produto e o usuario acredita que eh dele """
def recuperarProduto(request, achado_id):
	achado = Achado.objects.get(pk=achado_id)

	# XXX: Pegar usuario 
	u = User.objects.all()[0]

	recuperado = Recuperado(usuario=u, achado=achado, status=False)
	recuperado.save()

	return HttpResponse("Voce falou que o produto "+achado.produto.descricao+" eh seu.")

#uc09
""" Alguem perdeu algum produto e o usuario acredita que o achou """
def encontrarProduto(request, perdido_id):
	perdido = Perdido.objects.get(pk=perdido_id)

	# XXX: Pegar usuario 
	u = User.objects.all()[0]

	encontrado = Encontrado(usuario=u, perdido=perdido, status=False)
	encontrado.save()

	return HttpResponse("Voce disse que encontrou o produto %s" % perdido.produto.descricao)

#uc10 - busca por tipo ou periodo
def filtrarProduto(request):
	return HttpResponse("TEM QUE FAZER!!!")
