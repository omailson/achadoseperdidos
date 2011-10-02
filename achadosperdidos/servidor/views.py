# -*- coding: utf-8 -*-

from servidor.models import *
from django.core.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, Context, RequestContext

#TEM QUE TER CONTROLE DE ID!!!!!!!

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
def cadastrarProdutoPerdido(request):
	#TEM QUE TER CONTROLE DE ID!!!!!!!
	try:
		cadastro = request.POST
		idCadastro = "IDTEMPORARIO - TEM QUE MUDAR"
		tipoCadastro = cadastro['tipo']
		statusCadastro = False #false pra produto perdido, produto encontrado eh True
		descricaoCadastro = cadastro["descricao"]
		
		produto = Produto(id=idCadastro, tipo=tipoCadastro, status=statusCadastro, descricao=descricaoCadastro)
		produto.save()
		
		resposta = "Cadastro efetuado com sucesso."
	except:
		resposta = "Cadastro inv�lido. Digite os dados corretamente."

	return HttpResponse(resposta)

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
	produtos = Produto.objects.all()
	resposta = []

	for p in produtos:
		if (p.status == False):
			resposta.append(p)

	return HttpResponse(resposta)

#uc08 
def recuperarProduto(request):
	return HttpResponse("TEM QUE FAZER!!!")

#uc09
def encontrarProduto(request):
	return HttpResponse("TEM QUE FAZER!!!")

#uc10 - busca por tipo ou periodo
def filtrarProduto(request):
	return HttpResponse("TEM QUE FAZER!!!")
