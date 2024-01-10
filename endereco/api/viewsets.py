from rest_framework.viewsets import ModelViewSet
from .serializers import EnderecosSerializer
from endereco.models import Endereco


class EnderecosViewSets(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecosSerializer
    