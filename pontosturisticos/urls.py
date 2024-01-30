from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from core.api.viewsets import PontoTuristicoViewSets
from atracoes.api.viewsets import AtracaoViewSets
from endereco.api.viewsets import EnderecoViewSets
from comentarios.api.viewsets import ComentarioViewSets
from avaliacoes.api.viewsets import AvaliacaoViewSets
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()

router.register(r'pontoturistico', PontoTuristicoViewSets, basename='PontoTuristico')
router.register(r'atracoes', AtracaoViewSets)
router.register(r'enderecos', EnderecoViewSets)
router.register(r'comentarios', ComentarioViewSets)
router.register(r'avaliacoes', AvaliacaoViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
