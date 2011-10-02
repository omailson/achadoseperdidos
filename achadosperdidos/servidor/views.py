# -*- coding: utf-8 -*-

from servidor.models import *
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext

def index(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('index.html', c)

#uc-01 fazer login
def fazerLogin(request):
	t = loader.get_template('login.html')
	dados = request.POST
	login = dados['login']
	senha = dados['senha']
	
	
	
	c = RequestContext (request, {
		'mensagem': 'pegou'
	})
	return HttpResponse(t.render(c))
	
#uc-02 logout
def fazerLogout(request):
	return HttpResponse("TEM QUE FAZER!!!")

#uc-03 
def cadastrarUsuario(request):
	return HttpResponse("TEM QUE FAZER!!!")

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
		u = Usuario.objects.all()[0]

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
def recuperarProduto(request):
	return HttpResponse("TEM QUE FAZER!!!")

#uc09
def encontrarProduto(request):
	return HttpResponse("TEM QUE FAZER!!!")

#uc10 - busca por tipo ou periodo
def filtrarProduto(request):
	return HttpResponse("TEM QUE FAZER!!!")
