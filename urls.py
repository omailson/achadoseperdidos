from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from achadosperdidos.servidor.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'achadosperdidos.views.home', name='home'),
    # url(r'^achadosperdidos/', include('achadosperdidos.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^fazerLogin/$', 'achadosperdidos.servidor.views.fazerLogin'),
	url(r'^fazerLogout/$', 'achadosperdidos.servidor.views.fazerLogout'),
	url(r'^cadastrarUsuario/$', 'achadosperdidos.servidor.views.cadastrarUsuario'),
	url(r'^cadastrarProdutoEncontrado/$', 'achadosperdidos.servidor.views.cadastrarProdutoEncontrado'),
	url(r'^cadastrarProdutoPerdido/$', 'achadosperdidos.servidor.views.cadastrarProdutoPerdido'),
	url(r'^listarProdutosEncontrados/$', 'achadosperdidos.servidor.views.listarProdutosEncontrados'),
	url(r'^listarProdutosPerdidos/$', 'achadosperdidos.servidor.views.listarProdutosPerdidos'),
	url(r'^recuperarProduto/$', 'achadosperdidos.servidor.views.recuperarProduto'),
	url(r'^encontrarProduto/$', 'achadosperdidos.servidor.views.encontrarProduto'),
	url(r'^filtrarProduto/$', 'achadosperdidos.servidor.views.filtrarProduto'),
	url(r'^admin/', include(admin.site.urls)),
)
