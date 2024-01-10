from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSets
from django.conf.urls import include
from atracoes.api.viewsets import AtracoesViewSets
from endereco.api.viewsets import EnderecosViewSets
from comentarios.api.viewsets import ComentariosViewSets
from avaliacoes.api.viewsets import AvaliacoesViewSets

router = routers.DefaultRouter()

router.register(r'pontoturistico', PontoTuristicoViewSets)
router.register(r'atracoes', AtracoesViewSets)
router.register(r'enderecos', EnderecosViewSets)
router.register(r'comentarios', ComentariosViewSets)
router.register(r'avaliacoes', AvaliacoesViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
