from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecosSerializer
from endereco.models import Endereco


class EnderecoViewSets(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer
    