from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer


class AtracaoViewSets(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    