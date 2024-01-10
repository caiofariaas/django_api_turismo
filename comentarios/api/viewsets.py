from rest_framework.viewsets import ModelViewSet
from .serializers import ComentariosSerializer
from comentarios.models import Comentario


class ComentariosViewSets(ModelViewSet):
    queryset =  Comentario.objects.all()
    serializer_class = ComentariosSerializer
