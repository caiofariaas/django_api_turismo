from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSets
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSets)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
