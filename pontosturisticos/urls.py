from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSets
from django.conf.urls import include
from atracoes.api.viewsets import AtracaoViewSets
from endereco.api.viewsets import EnderecoViewSets
from comentarios.api.viewsets import ComentarioViewSets
from avaliacoes.api.viewsets import AvaliacaoViewSets

router = routers.DefaultRouter()

router.register(r'pontoturistico', PontoTuristicoViewSets)
router.register(r'atracoes', AtracaoViewSets)
router.register(r'enderecos', EnderecoViewSets)
router.register(r'comentarios', ComentarioViewSets)
router.register(r'avaliacoes', AvaliacaoViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
