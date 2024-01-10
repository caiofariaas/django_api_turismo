from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import Avaliacoes
from .serializers import AvaliacoesSerializer

class AvaliacaoViewSets(ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer
    